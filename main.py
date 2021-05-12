from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask Dockerized'

@app.route('/demo')
def demo():
    return render_template('home.html')

@app.route('/api/product', methods=['GET'])
def getMethod():
    # read somethin from database or file
    return jsonify('api-get(read)')

@app.route('/api/product', methods=['POST'])
def postMethod():
    # insert into database or write file
    return jsonify('api-post(create)')

@app.route('/api/product', methods=['PUT'])
def putMethod():
    # update something in database or file
    return jsonify('api-put(update)')

@app.route('/api/product', methods=['DELETE'])
def deleteMethod():
    # delete somthing in database or file
    return jsonify('api-delete(delete)')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
