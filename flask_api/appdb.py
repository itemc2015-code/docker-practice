import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db = mysql.connector.connect(
host=os.getenv('dbhostname'),
user=os.getenv('dbuser'),
password=os.getenv('dbpassword'),
database=os.getenv('dbdatabase')
)

# dbcursor.execute('create table users('
#                  'id int auto_increment primary key,'
#                  'name varchar(50),'
#                  'email varchar(100))')
# dbcursor.execute('show columns from users')

class Users:

    def view(self):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True,buffered=True)
        dbcursor.execute('select * from users')
        result = dbcursor.fetchall()
        dbcursor.close()
        return result
    
    def add(self,name,email):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True,buffered=True)
        querry = 'insert into users(name,email) values(%s,%s)'
        dbcursor.execute(querry,(name,email,))
        db.commit()
        dbcursor.close()

    def update(self,name,email,id):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True,buffered=True)
        querry = 'update users set name = %s, email = %s where id = %s'
        dbcursor.execute(querry,(name,email,id,))
        db.commit()
        dbcursor.close()

    def delete(self,id):
        db.ping(reconnect=True)
        dbcursor = db.cursor(dictionary=True,buffered=True)
        querry = 'delete from users where id = %s'
        dbcursor.execute(querry,(id,))
        db.commit()
        dbcursor.close()



