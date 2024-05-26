from flask import Flask, request, jsonify
from database.subroutines import user_subroutines

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

if __name__ == '__main__':
    app.run()