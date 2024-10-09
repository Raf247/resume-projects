# Import necessary libraries
import http.server
import socket
import socketserver
import webbrowser
import webbrowser
import pyqrcode
from pyqrcode import QRCode
import png
import os

# Set the port number for the HTTP server
PORT = 8010
os.environ['USERPROFILE']

# Retrieve the path to the user's desktop via the environment variable 'USERPROFILE'
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive')
os.chdir(desktop)

# Set up the HTTP request handler
Handler = http.server.SimpleHTTPRequestHandler
hostname = socket.gethostname() # Get the hostname of the machine

# Create a socket to find the local IP address by connecting to Google's DNS server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT) # Construct the URL
link = IP

# Create a QR code for the URL
url = pyqrcode.create(link)
url.svg("myqr.svg", scale = 8) # Save the QR code as an SVG file
webbrowser.open('myqr.svg') # Open the QR code SVG in the default web browser

# Set up and start the TCP server, serving HTTP requests
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Type this in your Browser", IP)
    print("or Use the QRCode")
    httpd.serve_forever() # Start the server and keep it running indefinitely