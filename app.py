# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return " Dockerize your Python app Exercise on WSL (Windows Linux)!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9091)
