"""Validate the canonical catalogue and reproduce all analysis exports (Python 3 stdlib)."""
import csv
import json
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def validate(d):
    assert d['schema_version'] == '1.0.0'
    ids = [s['id'] for s in d['systems']]
    assert len(ids) == len(set(ids)) and len(ids) >= 20
    for s in d['systems']:
        assert s['id'] and s['records'] and s['sources']
        assert date.fromisoformat(s['last_checked']) <= date.today()
        assert s['plans']['status'] in ('documented', 'conditional', 'not_confirmed')
        assert s['webhooks']['status'] in ('http', 'event_stream', 'conditional', 'not_confirmed', 'unavailable')
        refs = {r['id'] for r in s['sources']}
        assert len(refs) == len(s['sources'])
        for r in s['sources']:
            assert r['url'].startswith('https://') and r['checked_at'] == s['last_checked']
        for fact in [s['api'], s['plans'], s['webhooks'], s['authentication'], *s['records'], *s['limitations']]:
            assert fact['source_ids'] and set(fact['source_ids']) <= refs, (s['id'], fact)
        for r in s['records']:
            assert all(r[k] is None or type(r[k]) is bool for k in ('read','create','update'))
        v = s['verification']
        assert v['status'] in ('not_tested', 'tested')
        if v['status'] == 'tested':
            assert v['tested_at'] and v['test_scope'] and v['evidence_urls']
        else:
            assert v['tested_at'] is None and v['test_scope'] is None and not v['evidence_urls']
    return True

def csv_write(path, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    d=json.loads((ROOT/'data/integrations.json').read_text());validate(d)
    systems=[];capabilities=[];sources=[];claims=[]
    for s in d['systems']:
        systems.append(dict(id=s['id'],name=s['name'],category=s['category'],product_scope=s['product_scope'],api_status=s['api']['status'],api_style=s['api']['style'],plan_status=s['plans']['status'],minimum_plan=s['plans']['minimum_plan'],plan_notes=s['plans']['notes'],webhook_status=s['webhooks']['status'],webhook_notes=s['webhooks']['notes'],authentication_methods=' | '.join(s['authentication']['methods']),authentication_notes=s['authentication']['notes'],limitations=' | '.join(x['text'] for x in s['limitations']),ai_use_case_editorial=s['ai_use_case'],last_checked=s['last_checked'],verification_status=s['verification']['status'],tested_at=s['verification']['tested_at'],test_scope=s['verification']['test_scope'],source_count=len(s['sources']),detail_url=d['canonical_url']+'/'+s['id']))
        for i,r in enumerate(s['records']):
            capabilities.append(dict(system_id=s['id'],entity=r['entity'],read='unknown' if r['read'] is None else str(r['read']).lower(),create='unknown' if r['create'] is None else str(r['create']).lower(),update='unknown' if r['update'] is None else str(r['update']).lower(),notes=r['notes'],source_ids=' | '.join(r['source_ids']),verification_status=s['verification']['status']))
        sources += [dict(system_id=s['id'],**r) for r in s['sources']]
        for field in ('api','plans','webhooks','authentication'):
            claims += [dict(system_id=s['id'],claim_path=field,source_id=r) for r in s[field]['source_ids']]
        for field in ('records','limitations'):
            for i,v in enumerate(s[field]):
                claims += [dict(system_id=s['id'],claim_path=f'{field}[{i}]',source_id=r) for r in v['source_ids']]
    for name,rs in [('systems',systems),('capabilities',capabilities),('sources',sources),('claim_sources',claims)]:
        csv_write(ROOT/f'data/{name}.csv',rs)
    groups=[]
    for category in sorted({s['category'] for s in d['systems']}):
        rs=[s for s in d['systems'] if s['category']==category]
        groups.append(dict(category=category,systems=len(rs),http_webhooks=sum(s['webhooks']['status']=='http' for s in rs),conditional_webhooks=sum(s['webhooks']['status']=='conditional' for s in rs),event_stream=sum(s['webhooks']['status']=='event_stream' for s in rs),webhooks_unconfirmed=sum(s['webhooks']['status']=='not_confirmed' for s in rs),tested_connections=sum(s['verification']['status']=='tested' for s in rs)))
    csv_write(ROOT/'analysis/category_summary.csv',groups)
    print(json.dumps({'systems':len(systems),'record_groups':len(capabilities),'sources':len(sources),'claim_source_links':len(claims),'webhooks':dict(Counter(s['webhooks']['status'] for s in d['systems']))},indent=2))
if __name__ == '__main__': main()
