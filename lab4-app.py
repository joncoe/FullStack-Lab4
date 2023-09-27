from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        data = "hello world"
        return jsonify({"data": data})
    if(request.method == "POST"):
        data = request.get_json()
        return jsonify(data)

@app.route("/home/<int:num>", methods=["GET"])
def disp(num):
    return jsonify({'data': num * 2})

app.run(debug=True)
