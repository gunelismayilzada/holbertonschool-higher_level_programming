#!/usr/bin/python3
"""Module to implement http.server module"""
import http.server
import json


class HTTPHandler(http.server.BaseHTTPRequestHandler):
    """Simple Handler class inherited from BaseHTTPRequestHandler"""

    def _set_headers(self, status=200, content_type='text/plain'):
        """Helper method to send headers"""
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        """Method to handle GET requests"""

        if self.path == '/':
            self._set_headers(200, 'text/plain')
            self.wfile.write('Hello, this is a simple API!'.encode())

        elif self.path == '/data':
            self._set_headers(200, 'application/json')
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self._set_headers(200, 'text/plain')
            self.wfile.write("OK".encode('utf-8'))

        elif self.path == '/info':
            self._set_headers(200, 'application/json')
            data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(data).encode('utf-8'))

        else:
            self._set_headers(404, 'text/plain')
            self.wfile.write('Endpoint not found'.encode())


if __name__ == '__main__':
    server_address = ('', 8000)
    httpserver = http.server.HTTPServer(server_address, HTTPHandler)
    httpserver.serve_forever()
