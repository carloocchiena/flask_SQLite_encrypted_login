import sqlite3

DB = "D:\\Carlo\\Python\\Scripts\\web_app\\flask_SQLite_encrypted_login\\user_data.db"

# connect to our database and insert a new user
def insert_user(user_name, user_password, db=DB):
    """Insert user name and user password into DB
    :param user:
    :param password:
    :param db:
    :return: Ok msg if user inserted, Error msg if not
    """
    
    # connect to the database
    db_connection = None
    
    # try the query and commit
    try:
        db_connection = sqlite3.connect(db)
        cursor = db_connection.cursor()
     
        print("[*] DB Connection Successful!")
        
        sql = '''INSERT INTO users(username, password)
              VALUES(?,?)'''
        
        cursor.execute(sql, (user_name, user_password))
        db_connection.commit()
        db_connection.close()
        
        print("[*] User Inserted!")
        return "[*] User Inserted!"
    
    except ConnectionError as e:
        print(f"[!] DB connection aborted! Error:{e}")
        return f"[!] DB connection aborted! Error:{e}"
    
    except sqlite3.Error as e:
        print(f"[!] SQL error! Error:{e}")
        return f"[!] SQL error! Error:{e}"
    
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
        
        sql = '''SELECT rowid, username, password FROM users'''
            
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
    # insert_user("dummy_user", "admin")
    retrieve_users()
    