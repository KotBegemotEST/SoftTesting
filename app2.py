from flask import Flask, jsonify, request
import uuid, time

app = Flask(__name__)

USERS = {
    "alice@example.com": { "password": "pass123", "role": "user"},
    "admin@example.com": {"password":"admin1223","role": "admin"}
}

TOKENS = {

}


@app.get("/health")
def health():
    return jsonify({"ok":True})

@app.post("/login")
def login():
    data = request.get_json() or {}
    email = data.get("email")
    print(data)
    password = data.get("password")
    user = USERS.get(email)
    if not user or user["password"] != password:
        return jsonify({"error":"Credentials are bad"}), 401
    tok = str(uuid.uuid4())
    TOKENS[tok] = {'email':email, 'role': user['role']}
    time.sleep(0.15)
    return jsonify({'token':tok, 'role': user['role']})