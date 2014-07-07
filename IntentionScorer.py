from JobDurationExtractor import JobDurationExtractor
from LastJobStartDateExtractor import LastJobStartDateExtractor
from LastJobEndDateExtractor import LastJobEndDateExtractor
from EmploymentStatus import EmploymentStatus


class IntentionScorer:
        m_score = 0.0

        def __init__(self):
                self.m_score = 0.0
                # place holder for loading dictionaries
                # place holder for employment status model
                # place holder for profession model
                self.m_employment_status_ext = EmploymentStatus()
                self.m_duration_ext = JobDurationExtractor()
                self.m_last_start_ext = LastJobStartDateExtractor()
                self.m_last_end_ext = LastJobEndDateExtractor()


        def score(self, record):
                if self.m_employment_status_ext.value(record) == "unemployed":
                        self.m_score = 10.0
                else:
                        duration = self.m_duration_ext.get_numeric_value(record)
                        last_start = self.m_last_start_ext.get_numeric_value(record)
                        last_end = self.m_last_end_ext.get_numeric_value(record)
                        if last_end and last_start:
                                return (last_end - last_start) / duration * 10.0
                        return 5.0
