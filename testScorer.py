import simplejson as json
line = open("candidates.json", "r").readline()
candidates = json.loads(line)

from IntentionScorer import IntentionScorer
scorer = IntentionScorer()
for cand in candidates[0:100]: print scorer.score(cand)
