from flask import Flask
from flask import render_template

app = Flask("Hello")

@app.route("/hello")
def hello():
    return render_template('hello.html', name="Stefan")

@app.route("/tescht")
def test():
    return "succes"

if __name__ == "__main__":
    app.run(debug=True, port=5000)