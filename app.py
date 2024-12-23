from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock user data
users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = {"id": len(users) + 1, "name": data["name"]}
    users.append(user)
    return jsonify(user), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
