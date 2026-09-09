"""
HTTP Server implementation using Python standard library http.server.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from api.routes import handle_api_request


class APIRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)

    def do_GET(self):
        status_code, response_data = handle_api_request(self.path, method="GET")
        self._set_headers(status_code)
        self.wfile.write(json.dumps(response_data).encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_body = self.rfile.read(content_length) if content_length > 0 else b"{}"
        try:
            body_json = json.loads(post_body.decode("utf-8"))
        except json.JSONDecodeError:
            body_json = {}

        status_code, response_data = handle_api_request(self.path, method="POST", body_data=body_json)
        self._set_headers(status_code)
        self.wfile.write(json.dumps(response_data).encode("utf-8"))


def run_server(port=8080):
    server_address = ("", port)
    httpd = HTTPServer(server_address, APIRequestHandler)
    print(f"MATRIX2.0 API Server running on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
