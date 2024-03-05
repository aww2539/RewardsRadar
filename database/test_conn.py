from os import getenv
import pymysql
from dotenv import load_dotenv

load_dotenv()

# Set the database credentials
host = getenv('DB_HOST')
port = int(getenv('DB_PORT'))
user = getenv('DB_USER')
password = getenv('DB_PASSWORD')
database = getenv('DB_NAME')
test_table_name = getenv('TEST_DB_TABLE')

# Connect to the database
conn = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

# Create a cursor object
cursor = conn.cursor()

# Query to insert data
# insert_query = '''
#         INSERT INTO <table_name> (column_1, column_2, ...)
#         VALUES ("<col_1_value>", "<column_2_value>", ...)
#     '''

# Execute Insert
# cursor.execute(insert_query)

# Commit insert changes
# conn.commit()

# Query to insert data
select_query = '''
        SELECT *
        FROM {test_table_name}
        LIMIT 1
    '''.format(test_table_name=test_table_name)

# Execute select query
cursor.execute(select_query)

# Fetch the results
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)

# Close the cursor and connection
cursor.close()
conn.close()
