import simplejson as json
line = open("candidates.json", "r").readline()
candidates = json.loads(line)

def testNumericExtractor():
        from NumericExtractor import NumericExtractor
        testExtractor = NumericExtractor()
        for cand in candidates[0:10]:
                print testExtractor.name()
                print testExtractor.get_numeric_value(cand)

def testExperienceExtractor():
        from ExperienceExtractor import ExperienceExtractor
        testExtractor = ExperienceExtractor()
        for cand in candidates[0:10]:
                print testExtractor.name()
                print testExtractor.value(cand)

def testJobDurationExtractor():
        from JobDurationExtractor import JobDurationExtractor
        testExtractor = JobDurationExtractor()
        for cand in candidates[0:10]:
                print testExtractor.name()
                print testExtractor.value(cand)

def testExtractor(Extractor):
        test_extractor = Extractor()
        for cand in candidates[0:10]:
                print test_extractor.name()
                print test_extractor.value(cand)

testJobDurationExtractor()
from JobDurationExtractor import JobDurationExtractor
testExtractor(JobDurationExtractor)

from LastJobStartDateExtractor import LastJobStartDateExtractor
testExtractor(LastJobStartDateExtractor)

from LastJobEndDateExtractor import LastJobEndDateExtractor
testExtractor(LastJobEndDateExtractor)

