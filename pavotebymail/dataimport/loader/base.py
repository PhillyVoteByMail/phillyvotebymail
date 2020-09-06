import logging
from typing import List
import yaml
import arrow
from ..schemas import Schema

logger = logging.getLogger(__name__)

class BaseFieldParser(object):
    """Parse a line or blob of text for fields. We'll assume things are a line
    for now."""
    def parse_for_fields(self, blob: str) -> List[str]:
        return blob.split(',')


class DataLoader(object):
    """Loads data from a file into a dictionary"""

    @classmethod
    def load(cls, schema: Schema, data_path: str, field_parser: BaseFieldParser):
        loader = cls(schema, data_path, field_parser)
        return loader.process()

    def __init__(self, schema, data_path: str, field_parser: BaseFieldParser):
        self._field_parser = field_parser
        self._schema = schema
        self._data_path = data_path

    def process(self):
        """Default data processing opens a file and processes each line of the
        file as an item"""

        with open(self._data_path) as data:
            count = 0
            for line in data:
                item = dict()
                parsed_fields = self._field_parser.parse_for_fields(line)

                if len(parsed_fields) != len(self._schema.fields):
                    logger.warn("Skipping item. Does not match expected schema")
                    continue

                for i in range(len(parsed_fields)):
                    field_def = self.field_def(i)
                    item[field_def['field']] = self.type_translate(field_def['type'], parsed_fields[i])
                
                count += 1
                logger.info("loaded %s lines" % count)
                yield item

    def type_translate(self, type: str, value: str):
        if value == '':
            return None
        if type == 'String':
            return value
        if type == 'Date':
            return arrow.get(value, ['MM/DD/YYYY']).date()

        
    def field_def(self, index):
        return self._schema.fields[index]
