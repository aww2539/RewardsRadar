from os import getenv
from dotenv import load_dotenv
from pymysql import connect

load_dotenv()

host = getenv('DB_HOST')
port = int(getenv('DB_PORT'))
user = getenv('DB_USER')
password = getenv('DB_PASSWORD')
database = getenv('DB_NAME')
test_table_name = getenv('TEST_DB_TABLE')

conn = connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

def create_table():
    if conn.open:
        cursor = conn.cursor()

        create_statement = '''
            CREATE TABLE IF NOT EXISTS chase_cards (
                id MEDIUMINT NOT NULL AUTO_INCREMENT,
                card_id VARCHAR(255) NOT NULL,
                name TEXT NOT NULL,
                reward_1 TEXT,
                reward_2 TEXT,
                reward_3 TEXT,
                reward_4 TEXT,
                reward_5 TEXT,
                reward_6 TEXT,
                PRIMARY KEY (id),
                UNIQUE KEY (card_id)

            )
        '''
        cursor.execute(create_statement)
        print("Table created or already exists")
        cursor.close()
    else:
        print("Not connected to DB")

def insert_cards(card_dict):
    if conn.open:
        cursor = conn.cursor()

        insert_statement = '''
            INSERT IGNORE INTO chase_cards (
                card_id, name, reward_1, reward_2, reward_3, reward_4, reward_5, reward_6
            ) 
            VALUES (%s, %s, %s, %s, %s, %s ,%s, %s)
        '''

        cursor.executemany(insert_statement, card_dict)
        conn.commit()

        print("Cards inserted: ", conn.affected_rows())
        cursor.close()
    else:
        print("Not connected to DB")