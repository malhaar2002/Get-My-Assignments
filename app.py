from flask import Flask, jsonify
from main import getAssignments

app = Flask(__name__)

@app.route('/')
def getMyAssignments():
    return jsonify(getAssignments())

if __name__ == '__main__':
    app.run(debug = True)