# extract and analyze experience field
from JobTimeProfileExtractor import JobTimeProfileExtractor
from numbers import Number

class JobDurationExtractor(JobTimeProfileExtractor):
        m_name = "JobDurationExtractor"
        m_field = "experience"

        def meanJobDuration(self, timeProfiles):
                valid_time = []
                for time in timeProfiles:
                        if isinstance(time, Number):
                                valid_time.append(time)
                if valid_time == []: return None
                else: return sum(valid_time) / len(valid_time)

        def value(self, record):
                timeProfiles = JobTimeProfileExtractor.value(self, record)
                return self.meanJobDuration(timeProfiles)
