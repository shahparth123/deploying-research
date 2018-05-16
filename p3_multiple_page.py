# For creating simple web page we need to import flask 
from flask import Flask

#assign name to our flask application
#You can either use app's default name
app = Flask(__name__)

#or assign name yourself
#app = Flask("simple_hello_application")
@app.route('/')
def index():
    return 'Hello world'

@app.route('/cgpit')
def cgpit():
    return 'Hello CGPIT'

@app.route('/sttp')
def sttp():
    return 'Hello Python developers'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=9090)