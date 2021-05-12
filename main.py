from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask Dockerized'

@app.route('/demo')
def demo():
    return 'Hello World!'

@app.route('/api/product', methods=['GET'])
def getMethod():
    return 'api-get'

@app.route('/api/product', methods=['POST'])
def postMethod():
    return 'api-post'

@app.route('/apu/product', methods=['PUT'])
def putMethod():
    return 'api-put'

@app.route('/api/product', methods=['DELETE'])
def deleteMethod():
    return 'api-delete'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
