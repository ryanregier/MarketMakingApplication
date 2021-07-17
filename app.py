from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/<int:number>/')
def incrementer(number):
    return "Incremented number is " + str(number+1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
