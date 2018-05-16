# deploying-research
This repository contains tutorial to deploy any of your existing research into easily usable web services.

## Practical 1
This is simple python program to perform addition of two numbers.

```python
from __future__ import print_function
# to make sure print() on both python 2 and python 3 properly

#declare two numbers
number1 = 5
number2 = 10

#perform addition of two numbers
answer = number1 + number2

#print answer
print("Answer is:"+str(answer))

```
## Practical 2
In this code we will create simple webserver using Flask in python.
Page will simpaly display "Hello World as output"

```python
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
```

## Practical 3
In this code we add multiple page to practical 2. 

For doing that we need to add following code to practical 2:
```python
@app.route('/sttp')
def sttp():
    return 'Hello Python developers'

```

## Practical 4
In this practical we will handle GET, POST and JSON request using flask.
### 1.GET
We can handle get request either via query string or we can fetch values directly from url.
#### Get values from url
For this we can use <>.
```python
@app.route('/calculator/<a>/<b>')
def success(a,b):
   ans = int(a)+int(b)
   return 'answer is %s' % ans
```

#### Get values in query string
Syntax: request.args.get('parameter_name')
```python
@app.route('/calculator2', methods=['GET'])
def calc():
if request.method == 'GET':
      a = request.args.get('a')
      b = request.args.get('b')
      c=int(a)+int(b)
      return str(c)

```

### 2.POST
Syntax: request.form['parameter_name']
```python
@app.route('/calculator2', methods=['POST'])
def calc():
   if request.method == 'POST':
      a = request.form['a']
      b = request.form['b']
      c=int(a)+int(b)
      return str(c)

```

### 3.JSON using POST
Syntax:  request.get_json(silent=True, force=True)

silent for no warning

force for ignoring header type 

```python
@app.route('/jsondemo', methods=['POST', 'GET'])
def jsondemo():
    content = request.get_json(silent=True, force=True)
    return str( int(content['a']) + int(content['b']) )
```

## Practical 5 - Docker

### Install Docker
```shell
wget https://github.com/rancher/install-docker/blob/master/17.03.2.sh
sh rancherdockerinstall.sh
```

### Get all running containers

```shell
sudo docker ps -a
```
### Get all available docker images
```shell
sudo docker images
```

### Remove any image
```shell
sudo docker rmi IMAGE-ID
```

### Run new container
```shell
sudo docker run --name sttp shahparth123/apache:0.4
```
With more option
```shell
sudo docker run -d --restart=unless-stopped -it --name lab4 -v /home/parthpunita/demo/:/var/www/html -p 80:80 -p 443:443 -p 2022:22 shahparth123/apache:0.4
```
### Save container as image
```shell
sudo docker commit -a "Parth Shah" -m "demo server" lab5 shahparth123/apache:latest
```

### Remove Container
```shell
docker rm CONTAINER-ID/name
```