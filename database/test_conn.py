from os import getenv
import pymysql
from dotenv import load_dotenv

load_dotenv()
host = getenv('DB_HOST')
port = int(getenv('DB_PORT'))
user = getenv('DB_USER')
password = getenv('DB_PASSWORD')
database = getenv('DB_NAME')

def test_db_conn():

    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )

    if conn.open:
        print("Connected To Database: ", conn.host_info)
        conn.close()
    else:
        print("Connection Failed")
