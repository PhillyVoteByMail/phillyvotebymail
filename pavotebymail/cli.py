"""The main CLI for the application/worker
"""
import sys
import logging 
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pavotebymail.dataimport import voter_data_import
from pavotebymail.dataimport.db.db import ensure_db

root = logging.getLogger()
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


@click.group()
@click.option('--log-level', default='info')
def cli(log_level):
    root.setLevel(getattr(logging, log_level.upper()))


@cli.command()
@click.argument('voter_data_path', type=click.Path(exists=True, 
                dir_okay=False, resolve_path=True))
@click.option('--postgres-host', default='127.0.0.1')
@click.option('--postgres-port', type=click.INT, default=5432)
@click.option('--postgres-user', default='postgres')
@click.option('--postgres-password', default='postgres')
@click.option('--postgres-db', default='voters')
@click.option('--import-config', default='philadelphia')
def data_import(voter_data_path, postgres_host, postgres_port, 
                      postgres_user, postgres_password, postgres_db,
                      import_config):
    ensure_db(postgres_user, postgres_password, postgres_host, postgres_port, postgres_db)

    engine = create_engine('postgresql://%s:%s@%s:%d/%s' % (
        postgres_user,
        postgres_password,
        postgres_host,
        postgres_port,
        postgres_db
    ))
    Session = sessionmaker(bind=engine)
    session = Session()

    voter_data_import(engine, session, voter_data_path, import_config)
