import os
from flask import Flask, send_from_directory

app = Flask(__name__)

# Serve static files from the "cdn-images" folder
@app.route('/cdn-images/<path:filename>')
def serve_static(filename):
    return send_from_directory('cdn-images', filename)

@app.route('/')
def hello():
    return "Hello, World! Your static file server is ready!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
