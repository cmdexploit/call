from flask import Flask, request, jsonify, abort, render_template_string, send_from_directory

app = Flask(__name__)

# Define a hidden endpoint
@app.route('/hidden/flag', methods=['GET'])
def get_flag():
    user_agent = request.headers.get('User-Agent')
    if user_agent and 'curl' in user_agent:
        flag = "CTF{hidden_flag_123456}"
        return jsonify({"flag": flag})
    else:
        abort(403)

# Define a public endpoint with some basic information
@app.route('/', methods=['GET'])
def index():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hidden Flag Challenge</title>
        <style>
            /* General Reset */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            /* Body */
            body {
                font-family: 'Arial', sans-serif;
                background: #0e1a2b;
                color: #f0f4f8;
                line-height: 1.6;
            }

            /* Container */
            .container {
                width: 80%;
                margin: auto;
                overflow: hidden;
            }

            /* Header */
            header {
                background: #002d4f;
                color: #00bfae;
                padding: 20px 0;
                text-align: center;
                border-bottom: 3px solid #00bfae;
            }

            header h1 {
                font-size: 2.5em;
            }

            header p {
                font-size: 1.2em;
            }

            /* Info Section */
            .info {
                margin: 20px 0;
                padding: 20px;
                background: #003459;
                border-radius: 8px;
            }

            .info p {
                font-size: 1.2em;
            }

            /* Footer */
            footer {
                background: #002d4f;
                color: #00bfae;
                padding: 10px 0;
                text-align: center;
                border-top: 3px solid #00bfae;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>Welcome to the Hidden Flag Challenge!</h1>
                <p>Try to find the secret endpoint.</p>
            </header>
            <section class="info">
                <p>Explore the website and use your skills to uncover hidden secrets!</p>
            </section>
            <footer>
                <p>&copy; 2024 Hidden Flag Challenge. All rights reserved.</p>
            </footer>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
