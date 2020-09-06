from typing import List
from pavotebymail.dataimport.loader import BaseFieldParser

class FieldParser(BaseFieldParser):
    def parse_for_fields(self, blob) -> List[str]:
        split_by_tabs = blob.split('\t')
        return list(map(lambda a: a.strip('"'), split_by_tabs))
