# extrat the start date of last job
from ExperienceExtractor import ExperienceExtractor
from numbers import Number

class LastJobEndDateExtractor(ExperienceExtractor):
        m_name = "LastJobEndDateExtractor"

        def getEndDates(self, experiences):
                starts = []
                for exp in experiences:
                        start = exp.get("endDate", None)
                        if start <> None and isinstance(start, Number):
                                starts.append(start)
                return starts

        def value(self, record):
                experiences = ExperienceExtractor.value(self, record)
                startDates = self.getEndDates(experiences)
                if startDates <> []: return max(startDates)
                return None
