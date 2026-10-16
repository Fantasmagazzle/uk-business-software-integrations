import csv, io, importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('exporter', ROOT/'scripts/export.py'); exporter=importlib.util.module_from_spec(spec);spec.loader.exec_module(exporter)
class CatalogueTests(unittest.TestCase):
    def setUp(self):self.d=json.loads((ROOT/'data/integrations.json').read_text())
    def test_integrity(self):self.assertTrue(exporter.validate(self.d))
    def test_unsubstantiated_test_claim_is_rejected(self):
        self.d['systems'][0]['verification']['status']='tested'
        with self.assertRaises(AssertionError):exporter.validate(self.d)
    def test_dangling_citation_is_rejected(self):
        self.d['systems'][0]['plans']['source_ids']=['missing-source']
        with self.assertRaises(AssertionError):exporter.validate(self.d)
    def test_unknown_is_not_false_in_export(self):
        rows=list(csv.DictReader(io.StringIO((ROOT/'data/capabilities.csv').read_text())))
        index={(r['system_id'],r['entity']):r for r in rows}
        for s in self.d['systems']:
            for r in s['records']:
                for k in ['read','create','update']:
                    expected='unknown' if r[k] is None else str(r[k]).lower()
                    self.assertEqual(index[(s['id'],r['entity'])][k],expected)
    def test_summary_reconciles_without_claiming_unknown_as_absent(self):
        rows=list(csv.DictReader(io.StringIO((ROOT/'analysis/category_summary.csv').read_text())))
        self.assertEqual(sum(int(r['systems']) for r in rows),len(self.d['systems']))
        for r in rows:self.assertEqual(sum(int(r[k]) for k in ['http_webhooks','conditional_webhooks','event_stream','webhooks_unconfirmed']),int(r['systems']))
if __name__=='__main__':unittest.main()
