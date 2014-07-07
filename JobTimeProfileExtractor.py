# extract and analyze experience field
from ExperienceExtractor import ExperienceExtractor
from numbers import Number

class JobTimeProfileExtractor(ExperienceExtractor):
        m_name = "JobTimeProfileExtractor"

        def getTimeProfile(self, field):
                start = field.get("startDate", None)
                end = field.get("endDate", None)
                if start <> None and end <> None:
                        if isinstance(start, Number) and isinstance(end, Number):
                                return end - start
                        else:
                                return (start, end)
                return None

        def getTimeProfiles(self, fields):
                timeProfiles = []
                for field in fields:
                        profile = self.getTimeProfile(field)
                        if profile <> None:
                                timeProfiles.append(profile)
                return timeProfiles

        def value(self, record):
                fields = ExperienceExtractor.value(self, record)
                if fields <> []:
                        timeProfiles = self.getTimeProfiles(fields)
                return timeProfiles
