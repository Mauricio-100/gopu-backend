import http.server
import socketserver
import json
import os
import subprocess
import platform

PORT = 8080
TOKEN = "sk-agentic-🌟-gopu"

class GopuHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/status.json":
            cpu = os.getloadavg()[0] if hasattr(os, "getloadavg") else "N/A"
            ram = "N/A"
            if platform.system() == "Linux":
                with open("/proc/meminfo") as f:
                    lines = f.readlines()
                    mem_total = int(lines[0].split()[1])
                    mem_free = int(lines[1].split()[1])
                    ram = f"{100 - (mem_free / mem_total * 100):.2f}%"
            status = {
                "cpu": f"{cpu}",
                "ram": ram,
                "gpu": "Unavailable (no external deps)",
                "token": TOKEN,
                "modules": ["serve", "badge", "introspect", "ia-ready"]
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(status).encode("utf-8"))
        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            html = f"""
            <html><body style='background:#0f0f0f;color:#00ffcc;font-family:monospace;padding:2em'>
            <h1>🌐 GopuOS Agent Node</h1>
            <p>Status: ✅ Running on port {PORT}</p>
            <p>Token: <code>{TOKEN}</code></p>
            <p>Introspection: <code>badge --status --secure</code></p>
            <p>Modules: serve, badge, introspect, ia-ready</p>
            </body></html>
            """
            self.wfile.write(html.encode("utf-8"))
        else:
            self.send_error(404, "Not Found")

with socketserver.TCPServer(("", PORT), GopuHandler) as httpd:
    print(f"🚀 GopuOS Agent running on port {PORT}")
    try:
        # Optional: launch ngrok if available
        if os.path.exists("/usr/bin/ngrok"):
            subprocess.Popen(["/usr/bin/ngrok", "http", str(PORT)])
            print("🌍 ngrok tunnel launched")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 GopuOS Agent stopped.")
        httpd.server_close()
