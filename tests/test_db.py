from .tools import fixture_path 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, instrumentation
from sqlalchemy.orm.session import close_all_sessions
from sqlalchemy.ext.declarative import declarative_base
from pavotebymail.dataimport import load_config
from pavotebymail.dataimport.loader import DataLoader
from pavotebymail.dataimport.db.tables import create_class_from_schema
from pavotebymail.dataimport.db import Base


def test_philly_sql_table():
    _, schema = load_config('philadelphia')
    PhillyVoter = create_class_from_schema('PhillyVoter', 'philly_voters', schema)
    assert PhillyVoter.__dict__['id_number'] is not None
    assert PhillyVoter.__dict__['home_phone'] is not None


class TestPostgres(object):
    def setup(self):
        root_engine = create_engine('postgresql://postgres:example@127.0.0.1:5432/postgres')
        root_conn = root_engine.connect()
        root_conn.execute('commit')

        try:
            root_conn.execute('drop database test_db')
        except:
            pass
        root_conn.execute('commit')
            
        root_conn.execute('create database test_db')
        root_conn.close()

        self.field_parser, self.schema = load_config('philadelphia')

        self.engine = create_engine('postgresql://postgres:example@127.0.0.1:5432/test_db')
        self.base_class = declarative_base()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.PhillyVoter = create_class_from_schema('PhillyVoter', 'philly_voters', self.schema, base_class=self.base_class)

        self.base_class.metadata.create_all(self.engine)

    def teardown(self):
        # Close the current connection
        close_all_sessions()
        self.engine.dispose()
        
        root_engine = create_engine('postgresql://postgres:example@127.0.0.1:5432/postgres')
        root_conn = root_engine.connect()
        root_conn.execute('commit')
        root_conn.execute('drop database test_db')
        root_conn.close()
        
    def test_add_to_database(self):
        voter = self.PhillyVoter(id_number='11123334-41')

        self.session.add(voter)
        self.session.commit()

    def test_adding_fixtures_to_database(self):
        philly_test_path = fixture_path('philly_schema_test.txt')
        field_parser, schema = load_config('philadelphia')

        items = DataLoader.load(schema, philly_test_path, field_parser)
    
        for item in items:
            voter = self.PhillyVoter(**item)
            self.session.add(voter)
        self.session.commit()

        voters = list(self.session.query(self.PhillyVoter).order_by(self.PhillyVoter.id_number))
        assert voters[0].first_name == 'BILL'
        assert voters[1].first_name == 'STAPLER'
