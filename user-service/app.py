#1111111111111111111111111111
# from flask import Flask, jsonify, request
# import json
# import os

# app = Flask(__name__)
# DATA_FILE = os.path.join(os.path.dirname(__file__), 'users.json')


# def read_users():
#     with open(DATA_FILE, 'r', encoding='utf-8') as f:
#         return json.load(f)


# def write_users(users):
#     with open(DATA_FILE, 'w', encoding='utf-8') as f:
#         json.dump(users, f, ensure_ascii=False, indent=2)


# @app.get('/users')
# def get_users():
#     return jsonify(read_users())


# @app.get('/users/<int:user_id>')
# def get_user_by_id(user_id):
#     users = read_users()
#     user = next((u for u in users if u['id'] == user_id), None)
#     if not user:
#         return jsonify({'error': 'User not found'}), 404
#     return jsonify(user)


# @app.post('/users')
# def create_user():
#     data = request.get_json(silent=True) or {}
#     name = data.get('name')

#     if not name:
#         return jsonify({'error': 'Field "name" is required'}), 400

#     users = read_users()
#     new_id = max((u['id'] for u in users), default=0) + 1
#     new_user = {
#         'id': new_id,
#         'name': name,
#         'email': data.get('email', '')
#     }
#     users.append(new_user)
#     write_users(users)
#     return jsonify(new_user), 201


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=3001)


# 22222222222222222222222222222222222222
# from flask import Flask, jsonify
# import random

# app = Flask(__name__)

# @app.route('/data', methods=['GET'])
# def get_data():
#     number = random.randint(1, 100)
#     return jsonify({'value': number})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=3001)


#3333333333333333333333333333333333333
from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    number = random.randint(1, 100)
    return jsonify({'value': number})

# Добавляем корневой адрес для проверки
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'User Service работает! Используй /data'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)