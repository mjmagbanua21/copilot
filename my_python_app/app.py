from flask import Flask, request, jsonify, render_template
import random
import string
from flask import Flask, request, jsonify, render_template
import random
import string

app = Flask(__name__)

def generate_token():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/token', methods=['POST'])
def api_token():
    token = generate_token()
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(debug=True) 
