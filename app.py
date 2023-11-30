from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "John", "lastname": "Doe"},
    {"id": 2, "name": "Wojciech_Oczkowski", "lastname": "Najleprzy_nauczyciel_:)"},
    {"id": 3, "name": "Adrian", "lastname": "Trąbka"},
    {"id": 4, "name": "Mateusz", "lastname": "Informatyka"},
    {"id": 5, "name": "Klaudia", "lastname": "Tyc"}
]

@app.route("/home", methods=["POST"])
def hello():
    return "Hello World!"

@app.route("/users", methods=["GET"])
def get_user_list():
    return jsonify(users), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = find_user_by_id(user_id)
    if user:
        return jsonify(user), 200
    return jsonify(), 404

def find_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

if __name__ == "__main__" :
    app.run("localhost", 8083)
