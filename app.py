from flask import Flask, render_template, url_for
import socket

app = Flask(__name__)


# Home
@app.route('/') 
def home():
    hostname = socket.gethostname()
    IP = (socket.gethostbyname(hostname))
    print (IP)
    return render_template('home.html', title='Home', hostname=hostname, IP=IP)  

# Health
@app.route('/health') 
def health():
    return('<H1>Working! </H1>')   

@app.route('/about')
def about():
    return render_template('about.html', title='About')
 

@app.errorhandler(404)  
# inbuilt function which takes error as parameter 
def not_found(e): 
    return render_template('404.html', title='404',)   

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
