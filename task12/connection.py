import pymysql
import psycopg2

    
def connection_for_mysql(dbname = None):
    db = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "09888",
        database = dbname
    )
    cursor = db.cursor()
    db.autocommit = True
    return cursor


def connection_for_psql(dbname = 'postgres'):
    db = psycopg2.connect(
        database = dbname,
        user = "raj", 
        password = "09888", 
        host = "127.0.0.1", 
        port = "5432"
    )
    cursor = db.cursor()
    db.autocommit = True
    return cursor
