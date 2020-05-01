from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return ('Hello from Flask App! hostname: {}\n'.format(socket.gethostname()))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)