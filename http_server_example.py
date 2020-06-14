#handle a POST request
from flask import Flask, render_template, request, url_for, jsonify
app = Flask(__name__)


@app.route('/post/reply/misc/address', methods=['POST'])
def my_test_endpoint():
    input_json = request.get_json(force=True)
    # force=True is necessary if another developer forgot to set the MIME type to 'application/json'
    print('data from client:', str(input_json))
    dict_to_return = {'answer': 42}
    return jsonify(dict_to_return)


if __name__ == '__main__':
    app.run(debug=True)