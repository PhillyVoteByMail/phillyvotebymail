import os
import importlib
import yaml
from .loader import *
from .db import *
from .schemas import *
from sqlalchemy.orm import session, Session
from sqlalchemy.engine import Engine

CURR_FILE_DIR = os.path.dirname(os.path.realpath(__file__))

def voter_data_import(engine: Engine, session: Session, voter_data_path: str, config_name: str, commit_size=10000, base_class=Base):
    FieldParser, schema = load_config(config_name)

    voter_cls = create_class_from_schema('%sVoter' % config_name.capitalize(), config_name, 
                                         schema, base_class=base_class)
    base_class.metadata.create_all(engine)
    
    items = DataLoader.load(schema, voter_data_path, FieldParser)

    count = 0

    for item in items:
        if count > commit_size:
            session.commit()
            count = 0
        voter = voter_cls(**item)
        session.add(voter)
        count += 1
    session.commit()
        

def load_config(config_name: str) -> (BaseFieldParser, Schema):
    FieldParser = importlib.import_module('.configs.%s' % config_name, __name__).FieldParser

    # Load the schema
    schema = load_schema(config_name)
    return (FieldParser(), schema)

def load_schema(config_name: str) -> Schema:
    schema_path = os.path.join(CURR_FILE_DIR, 'configs', config_name, 'schema.yml')

    return Schema.load_raw(yaml.safe_load(open(schema_path)))
    