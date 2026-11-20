from flask import Flask, jsonify

app = Flask(__name__)

# Build RESTful APIs in Flask by using jsonify to return JSON responses for client requests
@app.route("/")
def json():
  marks = {
    "abhi" : 87,
    "raj" : 67,
    "samarth" : 43,
    "vishnu" : 98,
    "Rajath" : 100,
    "Reena" : 52
  }
  return jsonify(marks)

app.run(debug=True)

# ouptut
#{
#   "Rajath": 100,
#   "Reena": 52,
#   "abhi": 87,
#   "raj": 67,
#   "samarth": 43,
#   "vishnu": 98
# }