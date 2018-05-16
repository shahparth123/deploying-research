# For creating simple web page we need to import flask 
from flask import Flask

#assign name to our flask application
#You can either use app's default name
app = Flask(__name__)

#or assign name yourself
#app = Flask("simple_hello_application")

# define path on which application will respond and also create function to handle request
@app.route('/')
def index():
    #simply print "hello world"
    return 'Hello world'

if __name__ == '__main__':
    #if it is main program, run flask server on localhost with 9090 port number
    app.run(debug=True, host='0.0.0.0',port=9090)