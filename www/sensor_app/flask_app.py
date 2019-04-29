from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello_world():
    return "Hello World! Flask here"

@app.route("/data")
def show_data():
    return "<h1>Headline 1</h1><br><p>lots of cool shiny data here, come get it while its fresh!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)