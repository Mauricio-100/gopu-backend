from flask import Flask, jsonify
import psutil, subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><body style='background:#0f0f0f;color:#00ffcc;font-family:monospace;padding:2em'>
    <h1>🌐 GopuOS Agent Node</h1>
    <p>Status: ✅ Running</p>
    <p>Token: <code>sk-agentic-🌟-gopu</code></p>
    <p>Modules: serve, badge, introspect, ia-ready, terminal</p>
    <p><a href="https://localhost:7681" target="_blank">🖥️ Terminal Web</a></p>
    </body></html>
    """

@app.route('/status.json')
def status():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    try:
        gpu = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=utilization.gpu", "--format=csv,noheader,nounits"]
        ).decode().strip()
    except:
        gpu = "Unavailable"
    return jsonify({
        "cpu": f"{cpu}%",
        "ram": f"{ram}%",
        "gpu": f"{gpu}%",
        "token": "sk-agentic-🌟-gopu",
        "modules": ["serve", "badge", "introspect", "ia-ready", "terminal"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
