from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {
        "Hello":"World"
    }

@app.route("/root")
def root():
    return "<h1>Hello From Root</h1>"
if __name__ == '__main__':
    app.run()