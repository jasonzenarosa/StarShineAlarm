import sqlite3

def create_alarm(username:str, label:str, hour:int, minute:int, sound:str, triv_topic:str):
    '''creates new alarm, returns alarm id'''
    conn = sqlite3.connect('StarShine.db')
    cursor = conn.cursor()

    cmd = '''
    INSERT INTO Alarms (username, label, hour, minute, sound, triv_topic) 
        VALUES (?, ?, ?, ?, ?, ?)
    '''
    args = (username, label, hour, minute, sound, triv_topic)
    cursor.execute(cmd, args)

    alarm_id = cursor.lastrowid

    cursor.close()
    conn.commit()
    conn.close()

    return alarm_id