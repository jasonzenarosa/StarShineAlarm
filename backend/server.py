from flask import Flask, request, jsonify
from database.subroutines import user_subroutines, alarm_subroutines

app = Flask(__name__)

@app.route('/register', methods=['post'])
def register():
    data = request.json
    if 'username' in data:
        username = data['username']
    else:
        return jsonify({'code': 4})
    
    if 'password' in data:
        password = data['password']
    else:
        return jsonify({'code': 5})
    
    err = user_subroutines.create_user(username, password)

    return jsonify({"code": err})

@app.route('/new-alarm', methods=['post'])
def new_alarm():
    data = request.json

    username = data['username']
    label = data['label']
    hour = data['hour']
    minute = data['minute']
    sound = data['sound']
    triv_topic = data['triv_topic']

    alarm_id = alarm_subroutines.create_alarm(username, label, hour, minute, sound, triv_topic)
    return jsonify({'alarm_id': alarm_id})

if __name__ == '__main__':
    app.run()