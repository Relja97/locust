#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/endpoint_200':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')

        elif self.path == '/endpoint_401':
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b'Unauthorized')

        elif self.path == '/endpoint_403':
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b'Does not exist')

        elif self.path == '/endpoint_5xx':
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Internal Server Error')

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')

    def do_POST(self):
        if self.path == "/posting_200":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            # Here you can save the post_data into a variable if needed

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Write your response content here
            self.wfile.write(post_data.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"this route does not exist")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()