from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return ('<H1> Hello from Flask App! hostname: {}\n </H1>'.format(socket.gethostname()))
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
