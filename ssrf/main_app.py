from flask import Flask, request, render_template
import requests
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    url = request.form['url']
    
    # Adjust URL validation to allow specific internal addresses for the challenge
    if not re.match(r'^https?://', url):
        return render_template('index.html', response="Invalid URL format")

    # Allow access to specific internal addresses necessary for the challenge
    allowed_internal_addresses = [
        'http://127.0.0.1:8080/internal_api',
        'http://127.0.0.1:8080/hidden_admin_panel',
        'http://127.0.0.1:8080/fake_admin',
        'http://127.0.0.1:8080/real_admin'
    ]

    if url not in allowed_internal_addresses:
        return render_template('index.html', response="Access to internal addresses is restricted")

    try:
        response = requests.get(url)
        return render_template('index.html', response=response.text)
    except Exception as e:
        return render_template('index.html', response=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
