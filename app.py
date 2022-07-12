from flask import Flask
from flask_cors import CORS
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello"
CORS(app)

if __name__ == "__main__":
    app.run()
