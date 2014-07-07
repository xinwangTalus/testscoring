from Extractor import Extractor
from numbers import Number

class NumericExtractor(Extractor):
        m_name = "NumericExtractor"

        def checkValueType(self, val):
                return isinstance(val, Number)

        def get_numeric_value(self, record):
                val = self.value(record)
                if self.checkValueType(val):
                        return val
                try:
                        value = float(val)
                except ValueError:
                        return None
