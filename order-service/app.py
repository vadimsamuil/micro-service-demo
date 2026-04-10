#11111111111111111111111111111111111111
# from flask import Flask, jsonify, request
# import json
# import os
# import requests

# app = Flask(__name__)
# DATA_FILE = os.path.join(os.path.dirname(__file__), 'orders.json')
# USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://user-service:3001')


# def read_orders():
#     with open(DATA_FILE, 'r', encoding='utf-8') as f:
#         return json.load(f)


# def write_orders(orders):
#     with open(DATA_FILE, 'w', encoding='utf-8') as f:
#         json.dump(orders, f, ensure_ascii=False, indent=2)


# @app.get('/orders')
# def get_orders():
#     return jsonify(read_orders())


# @app.get('/orders/<int:order_id>')
# def get_order_by_id(order_id):
#     orders = read_orders()
#     order = next((o for o in orders if o['id'] == order_id), None)
#     if not order:
#         return jsonify({'error': 'Order not found'}), 404

#     try:
#         response = requests.get(f'{USER_SERVICE_URL}/users/{order["user_id"]}', timeout=5)
#         if response.status_code == 200:
#             user_data = response.json()
#         else:
#             user_data = {'error': 'User not found in user-service'}
#     except requests.RequestException:
#         user_data = {'error': 'Cannot connect to user-service'}

#     return jsonify({
#         'order': order,
#         'user': user_data
#     })


# @app.post('/orders')
# def create_order():
#     data = request.get_json(silent=True) or {}
#     user_id = data.get('user_id')
#     item = data.get('item')

#     if not user_id or not item:
#         return jsonify({'error': 'Fields "user_id" and "item" are required'}), 400

#     orders = read_orders()
#     new_id = max((o['id'] for o in orders), default=0) + 1
#     new_order = {
#         'id': new_id,
#         'user_id': user_id,
#         'item': item,
#         'amount': data.get('amount', 1)
#     }
#     orders.append(new_order)
#     write_orders(orders)
#     return jsonify(new_order), 201


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=3002)


#22222222222222222222222222222222222222
# from flask import Flask, jsonify
# import requests
# import time

# app = Flask(__name__)

# # Адрес первого сервиса (user-service)
# SERVICE_A_URL = "http://user-service:3001/data"

# @app.route('/fetch', methods=['GET'])
# def fetch_data():
#     try:
#         # Получаем данные от первого сервиса
#         response = requests.get(SERVICE_A_URL)
#         data = response.json()
        
#         # Сохраняем в лог-файл
#         with open('/logs/data.log', 'a') as f:
#             f.write(f"{time.ctime()} - Получено: {data}\n")
        
#         return jsonify({'status': 'ok', 'data': data})
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=3002)


#3333333333333333333333333333333333333
from flask import Flask, jsonify
import requests
import time

# app = Flask(__name__)

# # Адрес первого сервиса (user-service)
# SERVICE_A_URL = "http://user-service:3001/data"

# @app.route('/fetch', methods=['GET'])
# def fetch_data():
#     try:
#         # Получаем данные от первого сервиса
#         response = requests.get(SERVICE_A_URL)
#         data = response.json()
        
#         # Сохраняем в лог-файл
#         with open('/logs/data.log', 'a') as f:
#             f.write(f"{time.ctime()} - Получено: {data}\n")
        
#         return jsonify({'status': 'ok', 'data': data})
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)})

# # Добавляем корневой адрес для проверки
# @app.route('/', methods=['GET'])
# def home():
#     return jsonify({'message': 'Order Service работает! Используй /fetch'})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=3002)


from flask import Flask, jsonify
import requests
import time

app = Flask(__name__)

# Адрес первого сервиса (user-service)
SERVICE_A_URL = "http://user-service:3001/data"

@app.route('/fetch', methods=['GET'])
def fetch_data():
    try:
        # Получаем данные от первого сервиса
        response = requests.get(SERVICE_A_URL)
        data = response.json()
        
        # Сохраняем в лог-файл (теперь в /tmp)
        with open('/tmp/data.log', 'a') as f:
            f.write(f"{time.ctime()} - Получено: {data}\n")
        
        return jsonify({'status': 'ok', 'data': data})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Order Service работает! Используй /fetch'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3002)