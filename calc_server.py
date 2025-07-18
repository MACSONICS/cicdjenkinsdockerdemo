from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    msg='This an online calculator run as http://localhost:5000/add/2/3'
    
    return jsonify(msg)


@app.route('/add/<int:x>/<int:y>')
def add(x,y):
    return jsonify(result=x + y)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')


