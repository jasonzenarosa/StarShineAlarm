import sqlite3

USERNAME = 0
PASSWORD = 1

def create_user(username:str, password:str):
    '''returns 0 on success and 1 if username is taken'''

    conn = sqlite3.connect('StarShine.db')
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
        code = 0

    else:
        # username is not available
        code = 1

    cursor.close()
    conn.commit()
    conn.close()

    return code

def verify_user(username:str, password:int):
    '''return 0 on success, 1 if user doesn't exist, 2 if password is incorrect'''
    conn = sqlite3.connect('StarShine.db')
    cursor = conn.cursor()

    cmd = 'SELECT * FROM Users WHERE username = ?'
    cursor.execute(cmd, (username,))
    row = cursor.fetchone()

    code = 0

    if row is None:
        code = 1
    
    if row and (row[PASSWORD] != password):
        code = 2
    
    return code

if __name__ == "__main__":
    print(f"Creating user: test_username, test_password")
    code = create_user("test_username", "test_password")
    print(f"Code: {code}")

    print(f"Verifying user: test_username, test_password")
    code = verify_user("test_username", "test_password")
    print(f"Code: {code}")

    print(f"Verifying user: wrong_username, wrong_password")
    code = verify_user("wrong_username", "wrong_password")
    print(f"Code: {code}")

    print(f"Verifying user: test_username, wrong_password")
    code = verify_user("test_username", "wrong_password")
    print(f"Code: {code}")