from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load user data from the JSON file
with open('data/users.json', 'r') as f:
    users_data = json.load(f)


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users_data)


@app.route('/users/<username>', methods=['GET'])
def get_user_by_username(username):
    user = next((user for user in users_data if user['username'] == username), None) # noqa
    return jsonify(user) if user else ('', 404)


@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    users_data.append(new_user)
    with open('data/users.json', 'w') as f:
        json.dump(users_data, f, indent=4)
    return jsonify(new_user), 201


if __name__ == '__main__':
    app.run(debug=True)
