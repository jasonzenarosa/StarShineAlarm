import sqlite3

def create_user(username:str, password:int):
    '''returns 0 on success and 1 if username is taken'''

    conn = sqlite3.connect('database/StarShine.db')
    cursor = conn.cursor()

    cmd = 'SELECT * FROM Users WHERE username = ?'
    cursor.execute(cmd, (username,))

    if (cursor.fetchone() is None):
        # username is available
        cmd = '''
        INSERT INTO Users (username, password, language, timezone, theme, twentyfourhr) 
            VALUES (?, ?, ?, ?, ?, ?)
        '''
        args = (username, password, 'english', 'pst', 'venushacks', 0)
        cursor.execute(cmd, args)
        err = 0

    else:
        # username is not available
        err = 1

    cursor.close()
    conn.commit()
    conn.close()

    return err

if __name__ == "__main__":
    err = create_user("test_username", "test_password")
    print(f"Error Code: {err}")