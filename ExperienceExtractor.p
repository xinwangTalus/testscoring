# extract and analyze experience field
from NumericExtractor import NumericExtractor

class ExperienceExtractor(NumericExtractor):
        m_name = "ExperienceExtractor"
        m_field = "experience"

        def value(self, record):
                fields = record.get("experience", [])
                return fields
