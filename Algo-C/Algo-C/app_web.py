from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profil', methods=['POST'])
def profil():
    data = request.json

    return jsonify({"message": "Profil reçu"})

if __name__ == '__main__':
    app.run(debug=True)
