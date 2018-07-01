#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
from calculator import Calculator

class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):

        # ______________________________
        # Initialization

        self._set_response()

        # ______________________________
        # Parse URL to get parameters

        cleanPath = ""
        cleanPath = self.path
        cleanPath = cleanPath.replace("/?", "")
        params = urllib.parse.parse_qs(cleanPath)

        # ______________________________
        # Calculate result

        calc = Calculator()
        calc.add(int(params['a'][0]))
        calc.add(int(params['b'][0]))
        result = calc.getResult()

        # ______________________________
        # Write output

        output = str("<html><head><title>TEST</title></head><body>Result: " + str(result) + "</body></html>")
        self.wfile.write(output.format(self.path).encode('utf-8'))

    def do_POST(self):
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
