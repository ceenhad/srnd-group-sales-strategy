#!/usr/bin/env python3
"""Pull Mailchimp audiences, members and campaign reports into data/source/.

**The API key is never passed as an argument and never written to disk.** It is read from
the environment variable MAILCHIMP_API_KEY, so it cannot end up in shell history, in a
committed file, or in a chat transcript.

    setx MAILCHIMP_API_KEY "xxxxxxxx-us21"     # Windows, once — then reopen the terminal
    export MAILCHIMP_API_KEY="xxxxxxxx-us21"   # bash/zsh

    python data/fetch_mailchimp.py

The datacentre is the part after the dash in the key (us21, us14, …) and determines the
API host, so nothing else needs configuring.

Writes, with no key material in any of them:
    data/source/mailchimp-lists.json
    data/source/mailchimp-members-<list_id>.json
    data/source/mailchimp-campaigns.json

NOTE ON SCOPE: a classic Mailchimp API key has **full account access** — there is no
read-only variant. This script only issues GETs, but the key itself could do more. Create
a dedicated key for this, and revoke it afterwards if the pull is one-off.
"""
import os, sys, json, base64, urllib.request, urllib.parse, urllib.error

KEY = os.environ.get('MAILCHIMP_API_KEY', '').strip()
if not KEY:
    sys.exit('MAILCHIMP_API_KEY is not set in the environment. See the docstring above.')
if '-' not in KEY:
    sys.exit('Key looks malformed: expected "<key>-<dc>", e.g. abc123-us21.')

DC = KEY.rsplit('-', 1)[1]
BASE = f'https://{DC}.api.mailchimp.com/3.0'
AUTH = base64.b64encode(f'anystring:{KEY}'.encode()).decode()
OUT = 'data/source'


def get(path, **params):
    url = f'{BASE}{path}'
    if params:
        url += '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        'Authorization': f'Basic {AUTH}',
        'User-Agent': 'srnd-strategy-archive/1.0',
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        # deliberately does not echo the request URL, which carries no key but keeps habits tidy
        sys.exit(f'HTTP {e.code} on {path}: {e.read().decode()[:300]}')


def page(path, key, **params):
    """Walk Mailchimp's offset pagination and return every record."""
    out, offset = [], 0
    while True:
        d = get(path, count=1000, offset=offset, **params)
        batch = d.get(key, [])
        out += batch
        if len(batch) < 1000:
            return out
        offset += 1000


def write(name, obj):
    p = os.path.join(OUT, name)
    with open(p, 'w', encoding='utf-8') as fh:
        json.dump(obj, fh, indent=1)
    print(f'  {p}  ({len(obj) if isinstance(obj, list) else 1} records)')


def main():
    print(f'Mailchimp datacentre {DC}')

    lists = page('/lists', 'lists')
    write('mailchimp-lists.json', lists)
    for l in lists:
        print(f"    list: {l['name']!r}  members={l['stats']['member_count']}  "
              f"unsub={l['stats']['unsubscribe_count']}")

    for l in lists:
        members = page(f"/lists/{l['id']}/members", 'members',
                       fields='members.email_address,members.status,members.timestamp_opt,'
                              'members.last_changed,members.merge_fields,members.tags,'
                              'members.stats,total_items')
        write(f"mailchimp-members-{l['id']}.json", members)

    # per-campaign click detail: which URLs were actually clicked, and how often.
    # This is the demand signal — aggregate open/click rates say how many engaged,
    # the click URLs say what they engaged WITH.
    def click_details(sent_ids):
        out = []
        for cid in sent_ids:
            d = get(f'/reports/{cid}/click-details', count=1000)
            for u in d.get('urls_clicked', []):
                out.append(dict(campaign_id=cid, url=u.get('url'),
                                total_clicks=u.get('total_clicks'),
                                unique_clicks=u.get('unique_clicks'),
                                click_percentage=u.get('click_percentage')))
        return out

    campaigns = page('/campaigns', 'campaigns',
                     fields='campaigns.id,campaigns.web_id,campaigns.type,campaigns.status,'
                            'campaigns.send_time,campaigns.settings,campaigns.recipients,'
                            'campaigns.report_summary,total_items')
    write('mailchimp-campaigns.json', campaigns)
    sent = [c for c in campaigns if c.get('status') == 'sent']
    print(f'  campaigns: {len(campaigns)} total, {len(sent)} sent')

    clicks = click_details([c['id'] for c in sent])
    write('mailchimp-click-details.json', clicks)


if __name__ == '__main__':
    main()
