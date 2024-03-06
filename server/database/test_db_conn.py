from os import getenv
import pymysql
from dotenv import load_dotenv

load_dotenv()
DB_HOST = getenv('DB_HOST')
DB_PORT = int(getenv('DB_PORT'))
DB_USER = getenv('DB_USER')
DB_PASSWORD = getenv('DB_PASSWORD')
DB_NAME = getenv('DB_NAME')


def test_db_conn():

    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    if conn.open:
        print("Connected To Database: ", conn.host_info)
        conn.close()
    else:
        print("Connection Failed")
