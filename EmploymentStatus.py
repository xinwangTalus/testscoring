#employment status
from ExperienceExtractor import ExperienceExtractor
class EmploymentStatus(ExperienceExtractor):
        m_name = "EmploymentStatus"

        def value(self, record):
                return "employed"
