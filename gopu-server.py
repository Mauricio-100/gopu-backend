from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class GopuHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
              <title>GopuOS Agent Node</title>
              <style>
                body {{ background:#0f0f0f; color:#00ffcc; font-family:monospace; padding:2em; }}
                .badge {{ background:#222; border:1px solid #00ffcc; padding:1em; display:inline-block; }}
                .token {{ color:#ff00aa; font-weight:bold; }}
              </style>
            </head>
            <body>
              <h1>🌐 GopuOS Agent Node</h1>
              <p>Status: <span class="badge">✅ Running on port 8080</span></p>
              <p>Token: <span class="token">sk-agentic-🌟-gopu</span></p>
              <p>Introspection: <code>badge --status --secure</code></p>
              <p>Host: <code>{socket.gethostname()}</code></p>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404, "File not found")

def run():
    print("🚀 GopuOS Agent Node starting on port 8080...")
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, GopuHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 GopuOS Agent Node stopped.")
        httpd.server_close()

if __name__ == '__main__':
    run()
