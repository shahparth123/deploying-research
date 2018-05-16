from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/calculator/<a>/<b>')
def success(a,b):
   ans = int(a)+int(b)
   return 'answer is %s' % ans


@app.route('/calculator2', methods=['POST', 'GET'])
def calc():
   if request.method == 'POST':
      a = request.form['a']
      b = request.form['b']
      c=int(a)+int(b)
      return str(c)
   elif request.method == 'GET':
      a = request.args.get('a')
      b = request.args.get('b')
      c=int(a)+int(b)
      return str(c)

@app.route('/jsondemo', methods=['POST', 'GET'])
def jsondemo():
    content = request.get_json(silent=True, force=True)
    return str( int(content['a']) + int(content['b']) )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9090)
