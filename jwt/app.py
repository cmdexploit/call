# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template, abort
import jwt
import rsa
import time

app = Flask(__name__)

# Load RSA keys
with open('private.pem', 'rb') as f:
    PRIVATE_KEY = f.read()
with open('public.pem', 'rb') as f:
    PUBLIC_KEY = f.read()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# API Documentation route
@app.route('/api-docs')
def api_docs():
    return render_template('api_docs.html')

# Authentication route
@app.route('/auth', methods=['GET'])
def auth():
    name = request.args.get('name', '')
    if not name:
        return jsonify({"error": "Name parameter is required!"}), 400

    # Create JWT token
    payload = {
        "name": name,
        "type": "user",
        "iat": int(time.time()),
        "exp": int(time.time()) + 3600,
        "nonce": "5d41402abc4b2a76b9719d911017c592"
    }
    token = jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")
    
    # Return the token along with the message
    return jsonify({
        "message": "Authenticated successfully!",
        "token": token,
    })

# Normal user endpoint
@app.route('/api/normal', methods=['GET'])
def normal():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return abort(403)
    token = auth_header.split(" ")[1]
    try:
        decoded = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
        return jsonify({"message": "Congrats on authenticating! Too bad flags aren’t for normal users!"})
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired!"})
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token!"})

# Admin endpoint
@app.route('/api/admin', methods=['GET'])
def admin():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return abort(403)
    token = auth_header.split(" ")[1]
    key = request.args.get('key', '')
    if key != "PuNkSTarSsvK134":  
        return jsonify({"error": "Invalid key!"})
    try:
        decoded = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
        if decoded.get("type") == "admin":  
            return jsonify({"flag=": "CTF{Ultimate_JWT_Forgery_Mastery}"})
        else:
            return jsonify({"error": "You are not an admin!"})
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired!"})
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token!"})

if __name__ == '__main__':

    app.run(debug=True,port=5005)
