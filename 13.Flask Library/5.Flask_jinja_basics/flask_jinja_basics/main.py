from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "John": 45,
        "Saurabh": 99,
        "Mark": 45,
        "Jeff": 67,
        "Alexa": 90,
        "Lily": 100
    }
    return render_template("index.html", marks=marks)


app.run(debug=True)