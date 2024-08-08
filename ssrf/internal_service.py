from flask import Flask, render_template
import base64
import random

internal_app = Flask(__name__)

@internal_app.route('/')
def index():
    return render_template('internal_index.html')

@internal_app.route('/internal_api', methods=['GET'])
def internal_api():
    hints = [
        base64.b64encode(b"/hidden_admin_panel").decode('utf-8'),
        base64.b64encode(b"/fake_admin_panel").decode('utf-8'),
        base64.b64encode(b"/real_admin_panel").decode('utf-8')
    ]
    return f"Internal Data: Use this to access the admin panel: {random.choice(hints)}"

@internal_app.route('/hidden_admin_panel', methods=['GET'])
def hidden_admin_panel():
    return "Access denied. Only internal admin can access this panel."

@internal_app.route('/fake_admin', methods=['GET'])
def fake_admin():
    return "Welcome to the Fake Admin Panel. Nothing useful here."

@internal_app.route('/real_admin', methods=['GET'])
def real_admin():
    return "Congratulations! Here is your flag: CTF{ssrf_master_y0u_b3c0m3}"

if __name__ == '__main__':
    internal_app.run(port=8080, debug=True)
