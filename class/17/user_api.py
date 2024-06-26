from flask import Flask, request, jsonify
from flask_swagger import swagger

app = Flask(__name__)

users = []

@app.route('/spec')
def spec():
    swag = swagger(app)
    swag['info']['title'] = "User API"
    swag['info']['description'] = "API for managing users"
    swag['info']['version'] = "1.0.0"
    return jsonify(swag)

@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()
    users.append(user)
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is not None:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is not None:
        data = request.get_json()
        user.update(data)
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'User deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
