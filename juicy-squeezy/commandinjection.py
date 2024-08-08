import os
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Command Injection Challenge</title>
        <style>
            body {
                font-family: 'Courier New', Courier, monospace;
                background: #000;
                color: #00ff00;
                margin: 0;
                padding: 0;
                height: 100vh;
                overflow: hidden;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                position: relative;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 20px;
                color: #00ff00;
                text-shadow: 0 0 10px rgba(0, 255, 0, 0.8);
            }
            form {
                background: rgba(0, 0, 0, 0.8);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 15px rgba(0, 255, 0, 0.8);
                position: relative;
                z-index: 2;
            }
            label {
                display: block;
                font-size: 1.5em;
                margin-bottom: 15px;
            }
            input[type="text"] {
                width: 100%;
                padding: 15px;
                border: 2px solid #00ff00;
                border-radius: 10px;
                background: #000;
                color: #00ff00;
                font-size: 1.2em;
                margin-bottom: 15px;
                box-shadow: inset 0 0 5px rgba(0, 255, 0, 0.8);
            }
            input[type="submit"] {
                background: #00ff00;
                color: #000;
                border: none;
                padding: 15px 30px;
                font-size: 1.5em;
                cursor: pointer;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0, 255, 0, 0.8);
                transition: background 0.3s ease;
            }
            input[type="submit"]:hover {
                background: #00cc00;
            }
            pre {
                background: rgba(0, 0, 0, 0.8);
                color: #00ff00;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 0 15px rgba(0, 255, 0, 0.8);
                text-align: left;
                white-space: pre-wrap;
                word-wrap: break-word;
                position: relative;
                z-index: 2;
            }
            .matrix {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                overflow: hidden;
                z-index: 1;
            }
            .matrix-canvas {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: #000;
                z-index: 1;
            }
        </style>
    </head>
    <body>
        <canvas id="matrix" class="matrix-canvas"></canvas>
        <div>
            <h1>Command Injection Challenge</h1>
            <form action="/ping" method="get">
                <label for="ip">IP to ping:</label>
                <input type="text" id="ip" name="ip" placeholder="Enter IP address" required>
                <input type="submit" value="Ping">
            </form>
        </div>
        <script>
            // Matrix effect
            const canvas = document.getElementById('matrix');
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;

            const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
            const fontSize = 10;
            const columns = canvas.width / fontSize;
            const drops = Array.from({ length: columns }).fill(0);

            function drawMatrix() {
                ctx.fillStyle = 'rgba(0, 0, 0, 0.1)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);

                ctx.fillStyle = '#00ff00';
                ctx.font = `${fontSize}px monospace`;

                for (let i = 0; i < drops.length; i++) {
                    const text = chars[Math.floor(Math.random() * chars.length)];
                    ctx.fillText(text, i * fontSize, drops[i] * fontSize);
                    if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                        drops[i] = 0;
                    }
                    drops[i]++;
                }
            }

            setInterval(drawMatrix, 33);
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip')
    if not ip:
        return "IP address is required", 400
    result = os.popen(f"ping -c 1 {ip}").read()
    return f"<pre>{result}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
