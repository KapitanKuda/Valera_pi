from flask import Flask
from flask import request

import datetime




app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'


@app.route('/group_start', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        file = request.args.get('file', '')
        link = request.args.get('link', '')
        now = datetime.datetime.now()
        hardware= request.args.get('hardware','')
        f = open('text.txt', 'a')
        f.write(file+";"+link+";"+hardware+";"+now+'\n')
        f.close()
    return "good"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
