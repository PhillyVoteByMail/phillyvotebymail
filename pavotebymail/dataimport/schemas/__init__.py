class Schema(object):
    @classmethod
    def load_raw(cls, raw_schema) -> 'Schema':
        fields = []

        for field_def in raw_schema['fields']:
            field = field_def['field'].lower().replace(' ', '_')
            fields.append(dict(
                field=field,
                type=field_def['type'],
                is_primary_key=field_def.get('is_primary_key', False)
            ))


        return cls(fields)

    def __init__(self, fields):
        self._fields = fields

    @property
    def fields(self):
        return self._fields

    @property
    def primary_key_name(self):
        primary_key = list(filter(lambda a: a.get('is_primary_key', False), self.fields))
        if len(primary_key) != 1:
            raise Exception('Schema does not have a primary key')
            
        return primary_key[0]['field']


