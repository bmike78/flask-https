from flask import Flask 
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.load_cert_chain('server.crt', 'server.key')

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask is running!'

if __name__ == '__main__':  
     app.run(host='0.0.0.0', port=443, threaded=True, debug=True, ssl_context=context)
