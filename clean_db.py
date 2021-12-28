import sqlite3


DB = "user_data.db"

# clean the database
def clean_db(db=DB):
    """Clean the database
    """
    db_connection = None
    
    try:
        db_connection = sqlite3.connect(db)
        cursor = db_connection.cursor()
     
        print("[*] DB Connection Successful!")
        
        sql = '''DELETE FROM users'''
        
        cursor.execute(sql,)
        db_connection.commit()
        print("[*] DB Cleaned!")
        db_connection.close()
        
        return True
    
    except ConnectionError as e:
        print(f"[!] DB connection aborted! Error:{e}")
        return False

# call the functions
if __name__ == '__main__':
    clean_db()
    