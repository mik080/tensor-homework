#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading, time, datetime
import signal

hostName = ""
serverPort = 80

quit_event = threading.Event()
signal.signal(signal.SIGTERM, lambda *_args: quit_event.set())

class MyServer(BaseHTTPRequestHandler):    
        def do_GET(self):            
            if quit_event.is_set()==False:
                self.get_time=datetime.datetime.now().strftime("%H:%M:%S")
                time.sleep(10)                
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()                
                self.wfile.write(bytes( self.get_time,  "utf-8"))                             
            else:
                self.send_response(503)
                self.end_headers()                                
                
class ThreadingSimpleServer(ThreadingMixIn,HTTPServer):    
    pass

if __name__ == "__main__":
    webServer = ThreadingSimpleServer((hostName, serverPort), MyServer)    
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()

    