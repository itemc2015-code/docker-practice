import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db = mysql.connector.connect(
host=os.getenv('dbhostname'),
user=os.getenv('dbuser'),
password=os.getenv('dbpassword')
)
dbcursor = db.cursor(dictionary=True)

dbcursor.execute('show databases')
result=dbcursor.fetchall()
print(result)
