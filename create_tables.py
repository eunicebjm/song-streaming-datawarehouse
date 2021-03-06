import psycopg2
from sql_queries import create_table_queries, drop_table_queries

import json
# load configurations
with open('config.json') as f:
    config = f.read()
config = json.loads(config)

def create_database():
    # connect to default database
    conn = psycopg2.connect("host={hostname} dbname={dbname} user={username} password={password}".format(
        hostname= config.get("HOSTNAME"),
        dbname= config.get("DB-NAME"),
        username= config.get("USERNAME"),
        password=config.get("PASSWORD")
    ))
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS {dbname}".format(
        dbname = config.get("DB-NAME")
    ))
    cur.execute("CREATE DATABASE {dbname} WITH ENCODING 'utf8' TEMPLATE template0".format(
        dbname = config.get("DB-NAME")
    ))

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host={hostname} dbname={dbname} user={username} password={password}")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()