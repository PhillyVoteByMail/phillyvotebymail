import psycopg2

def ensure_db(user, password, host, port, db_name: str):
    """Ensures a database exists in the postgresql server"""

    connection = psycopg2.connect(
        database='postgres',
        user=user, 
        password=password, 
        host=host, 
        port=port
    )
    cursor = connection.cursor()
    cursor.execute('commit')

    # Check that the database exists
    cursor.execute("""SELECT datname FROM pg_database WHERE datistemplate = false""")
    exists = False
    for table in cursor.fetchall():
        if table[0] == db_name:
            exists = True
            break
    
    # Create if it does not
    if not exists:
        cursor.execute('create database %s' % db_name)

