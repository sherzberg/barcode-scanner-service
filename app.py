from flask import Flask, jsonify, request

import bcservice


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Please post to /image with mutli-part form and a "file" attribute.'


@app.route('/image', methods=['POST'])
def get_barcdes():
    f = request.files['file']
    result = bcservice.scan_image(f)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
