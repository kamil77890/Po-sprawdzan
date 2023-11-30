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

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if "name" in data and "lastname" in data:
        new_user = {
            "id": len(users) + 1,
            "name": data["name"],
            "lastname": data["lastname"]
        }
        users.append(new_user)
        return jsonify({"id": new_user["id"]}), 201
    return jsonify(), 400

@app.route("/users/<int:user_id>", methods=["PATCH"])
def update_user_partial(user_id):
    user = find_user_by_id(user_id)
    if user:
        data = request.get_json()
        user["name"] = data.get("name", user["name"])
        user["lastname"] = data.get("lastname", user["lastname"])
        return "easterEgg +1 za spostegawczosć i na sprawdzianie ;)", 204
    return jsonify(), 404

@app.route("/users/<int:user_id>", methods=["PUT"])
def create_or_update_user(user_id):
    user = find_user_by_id(user_id)
    data = request.get_json()
    if user:
        user["name"] = data.get("name", user["name"])
        user["lastname"] = data.get("lastname", user["lastname"])
        return " have no idea what's wrong with me :(", 204
    elif "name" in data and "lastname" in data:
        new_user = {
            "id": user_id,
            "name": data["name"],
            "lastname": data["lastname"]
        }
        users.append(new_user)
        return jsonify({"id": new_user["id"]}), 201
    return jsonify(), 400

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = find_user_by_id(user_id)
    if user:
        users.remove(user)
        return jsonify(), 204
    return jsonify(), 404

def find_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

if __name__ == "__main__":
    app.run("localhost", 8083)
