from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class JSONHandler(BaseHTTPRequestHandler):

    def __set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        self.__set_response()
        output_json = json.dumps(["key", "val"])
        self.wfile.write(output_json.format(self.path).encode("utf-8"))

    def do_POST(self):
        self.__set_response()
        self.wfile.write("test".format(self.path).encode("utf-8"))


class JSONServer():

    __SERVER_ADDRESS = ""
    __PORT = 8080

    def start_server(self):
        server_address = (self.__SERVER_ADDRESS, self.__PORT)
        server_class = HTTPServer
        httpd = server_class(server_address, JSONHandler)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()