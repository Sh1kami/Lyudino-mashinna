import unittest,tempfile
from pathlib import Path
from research_metrics import sus_score,aggregate
class MetricsTest(unittest.TestCase):
 def test_sus_extremes(self):
  self.assertEqual(sus_score([5,1]*5),100)
  self.assertEqual(sus_score([1,5]*5),0)
  self.assertEqual(sus_score([3]*10),50)
 def test_invalid_answers(self):
  for vals in [[1]*9,[6]*10,[True]*10]:
   with self.assertRaises(ValueError):sus_score(vals)
 def test_empty_is_not_zero(self):
  with tempfile.TemporaryDirectory() as d:
   s=Path(d)/'sessions.csv';u=Path(d)/'sus.csv';s.write_text('participant_id,task_id,success,seconds\n');u.write_text('participant_id,'+','.join('q'+str(i) for i in range(1,11))+'\n');result=aggregate(s,u);self.assertIsNone(result['TCR_percent']);self.assertIsNone(result['SUS_mean']);self.assertFalse(result['ready_for_lab7'])
if __name__=='__main__':unittest.main()
