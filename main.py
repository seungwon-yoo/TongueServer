from flask_cors import CORS
from flask import Flask, request, jsonify, send_file, Blueprint

# Flask 인스턴스 정리
app = Flask(__name__)
CORS(app)


@app.route('/download', methods=['GET'])
def download():
    id = request.args.get('id')
    filePath = "./sample/" + id + ".png"
    return send_file(filePath, mimetype='image/jpg')


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['image']  # 파일 받기

    id = request.args.get('id')
    filePath = "./sample/" + id + ".png"
    f.save(filePath)

    json = {
        'url': filePath
    }

    return jsonify(json)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
