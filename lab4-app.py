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

@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        data_id = request.form.get('Id')
        data_customer = request.form.get('Customer')
        data_quantity = request.form.get('Quantity')
        data_price = request.form.get('Price')
        print('Id: ', data_id)
        print('Customer', data_customer)
        print('Quantity', data_quantity)
        print('Price', data_price)
        return jsonify({'data': 'success'})

@app.route("/home/<int:num>", methods=["GET"])
def disp(num):
    return jsonify({'data': num * 2})

app.run(debug=True)
