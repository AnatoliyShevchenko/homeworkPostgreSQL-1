import psycopg2
from psycopg2 import Error
from psycopg2.extensions import (connection, ISOLATION_LEVEL_AUTOCOMMIT)
from dotenv import load_dotenv
import os


try:
    load_dotenv()
    connection: connection = psycopg2.connect(
        user=os.environ.get('USER'),
        password=os.environ.get('PASSWORD'),
        host=os.environ.get('HOST'),
        port=os.environ.get('PORT'),
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    print('Connection Successful')
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE Homework;")
    print('Database is successful created!')

except (Exception, Error) as e:
    print('Connection error: {}'.format(e))

finally:
    cursor.close()
    connection.close()
    print("Connection is close")