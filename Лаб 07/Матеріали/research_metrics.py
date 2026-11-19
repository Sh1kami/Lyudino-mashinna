"""Validate and aggregate real research CSV files. Empty inputs stay empty."""
from pathlib import Path
import csv,json,statistics,argparse
def sus_score(values):
 if len(values)!=10 or any(type(v) is not int or not 1<=v<=5 for v in values):raise ValueError('SUS requires ten integers from 1 through 5')
 return 2.5*sum(v-1 if i%2==0 else 5-v for i,v in enumerate(values))
def aggregate(sessions,sus):
 with Path(sessions).open(encoding='utf-8-sig') as f:rows=list(csv.DictReader(f))
 with Path(sus).open(encoding='utf-8-sig') as f:answers=list(csv.DictReader(f))
 byperson={}
 for r in rows:
  person=r['participant_id'];task=r['task_id'];key=(person,task)
  if not person or task not in {'T1','T2','T3','T4'}:raise ValueError('Invalid participant/task ID')
  if key in byperson:raise ValueError('Duplicate task result')
  if r['success'] not in {'0','1'} or float(r['seconds'])<0:raise ValueError('Invalid outcome or duration')
  byperson[key]=r
 scores={}
 for r in answers:
  if r['participant_id'] in scores:raise ValueError('Duplicate SUS respondent')
  scores[r['participant_id']]=sus_score([int(r['q'+str(i)]) for i in range(1,11)])
 persons={x[0] for x in byperson}
 complete=sorted(p for p in persons if all((p,t) in byperson for t in ['T1','T2','T3','T4']))
 return {'participants':len(persons),'complete_sessions':complete,'attempts':len(rows),'TCR_percent':100*sum(int(r['success']) for r in rows)/len(rows) if rows else None,'SUS_individual':scores,'SUS_mean':statistics.mean(scores.values()) if scores else None,'ready_for_lab7':len(complete)>=3 and all(p in scores for p in complete)}
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('sessions');ap.add_argument('sus');ap.add_argument('--output',default='metrics.json');a=ap.parse_args();data=aggregate(a.sessions,a.sus);Path(a.output).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(data,ensure_ascii=False,indent=2))
