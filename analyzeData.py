import simplejson as json
line = open("candidates.json", "r").readline()
candidates = json.loads(line)

emptyLineCnt = 0
emptyFirstCnt = 0
emptyLastCnt = 0

def isEmptyField(can, key):
        result = True
        if can.has_key(key):
                val = can[key]
                if isinstance(val, str): result = val.strip() == ""
                elif isinstance(val, list): result = val == []
                elif isinstance(val, dict): result = val == {}
                else: result = val == None
        return result

fieldValCnts = {}
for cand in candidates:
        first = cand.get("firstName", "")
        middle = cand.get("middleName", "")
        last = cand.get("lastName", "")
        if first == "": emptyFirstCnt += 1
        if last == "": emptyLastCnt += 1
        if first + middle + last == "": emptyLineCnt += 1
        for key in cand.keys():
                if not isEmptyField(cand, key):
                        if key == "skills":
                                print cand[key]
                                input()
                        if fieldValCnts.has_key(key): fieldValCnts[key] += 1
                        else: fieldValCnts[key] =1

print emptyLineCnt, emptyFirstCnt, emptyLastCnt
for key, cnt in fieldValCnts.items():
        print key, cnt
