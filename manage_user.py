import sqlite3
from datetime import date

DB = "D:\\Carlo\\Python\\Scripts\\web_app\\flask_db\\users.db"
TODAY = date.today()

# connect to our database and insert a new user
def insert_user(user, db=DB, date=TODAY):
    """Create a new user into the users table
    :param user:
    :param db:
    :param today:
    :return: user, date
    """
    db_connection = None
    
    try:
        db_connection = sqlite3.connect(db)
        cursor = db_connection.cursor()
     
        print("[*] DB Connection Successful!")
        
        sql = '''INSERT INTO users(entry_date, user)
              VALUES(?,?)'''
        
        cursor.execute(sql, (date, user))
        db_connection.commit()
        print("[*] User Inserted!")
        db_connection.close()
        
        return date, user
    
    except Exception as e:
        print(f"[!] DB connection aborted! Error:{e}")
        return f"[!] DB connection aborted! Error:{e}"
    
def retrieve_users(db=DB):
    """Retrieve all users from the users table
    :param db:
    :return: users
    """
    db_connection = None
    
    try:
        db_connection = sqlite3.connect(db)
        cursor = db_connection.cursor()
        
        print("[*] DB Connection Successful!")
        
        sql = '''SELECT rowid, entry_date, user FROM users'''
            
        cursor.execute(sql)
        users = cursor.fetchall()
        db_connection.commit()
        print("[*] Users Retrieved!")
        db_connection.close()
        
        return users
    
    except Exception as e:
        print(f"[!] DB connection aborted! Error:{e}")
        return f"[!] DB connection aborted! Error:{e}"

if __name__ == '__main__':
    insert_user("dummy_user")
