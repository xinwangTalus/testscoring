# extrat the start date of last job
from ExperienceExtractor import ExperienceExtractor
from numbers import Number

class LastJobStartDateExtractor(ExperienceExtractor):
        m_name = "LastJobStartDateExtractor"

        def getStartDates(self, experiences):
                starts = []
                for exp in experiences:
                        start = exp.get("startDate", None)
                        if start <> None and isinstance(start, Number):
                                starts.append(start)
                return starts

        def value(self, record):
                experiences = ExperienceExtractor.value(self, record)
                startDates = self.getStartDates(experiences)
                if startDates <> []: return max(startDates)
                return None
