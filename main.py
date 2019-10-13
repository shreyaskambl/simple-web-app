#!/usr/bin/env python                                                  
                                                                        
from http.server import BaseHTTPRequestHandler, HTTPServer             
                                                                        
class handler(BaseHTTPRequestHandler):                                 
    def do_GET(self):                                                    
        self.send_response(200)                                            
        self.send_header('Content-type','text/plain')                      
        self.end_headers()                                      
        message = "Hello world v1!\n"                                      
        self.wfile.write(bytes(message, "utf8"))                           
                                                                        
if __name__ == '__main__':                                             
    httpd = HTTPServer(('0.0.0.0', 8000), handler)                       
    httpd.serve_forever()
