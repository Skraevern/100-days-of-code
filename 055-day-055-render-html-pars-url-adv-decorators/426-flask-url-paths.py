from flask import Flask

app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/")
def hello_world():
    return "hello_world"

# http://127.0.0.1:5000/bye
@app.route("/bye")
def bye():
    return "Bye"

@app.route("")
def greet(name):
    return f"Hello {name}"

if __name__ == "__main__":
    app.run()