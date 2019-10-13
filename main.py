from prometheus_client import start_http_server, Gauge, MetricsHandler
from http.server import BaseHTTPRequestHandler, HTTPServer      

class HTTPRequestHandler(MetricsHandler):

    HTTP_REQUEST_COUNT = Gauge('http_request_count', 'HTTP Request Count')
    def do_GET(self):
        if self.path == '/':
            self.HTTP_REQUEST_COUNT.inc()
            return self.get_main()
        elif self.path == '/metrics':
            return super(HTTPRequestHandler, self).do_GET()
                  
    def get_main(self):                     
        self.send_response(200)                                            
        self.send_header('Content-type','text/plain')                      
        self.end_headers()                                                          
        self.wfile.write(b"<html><head>Title</head><body><p>This is a test.</p></body></html>")
        #self.wfile.close()

if __name__ == "__main__":
    server_address = ('', 8000)
    HTTPServer(server_address, HTTPRequestHandler).serve_forever()
