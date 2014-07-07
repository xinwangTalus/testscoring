# Base Class for FeatureExtractors

class Extractor:
        m_name = "AbstractExtractor"
        m_field = "_id"

        def name(self):
                return self.m_name

        def value(self, record):
                val = None
                if record.has_key(self.m_field):
                        field = record[self.m_field]
                        if isinstance(field, dict) and field.has_key("str"):
                                val = field["str"]
                return val

