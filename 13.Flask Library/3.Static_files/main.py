from flask import Flask,render_template,send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download/<path:filename>")
def download_file(filename):
    return send_from_directory(app.static_folder, filename, as_attachment=True)

app.run(port=5000,debug=True)

# accessing static files : http://localhost:5000/static/SYNOPSIS_MAX.pdf
# and for videos it goes like localhost:5000/static/sample1.mp4 so on 
# here static is files folder name and they will be available for everyone

# Note ->  only static files can be accessed by public the confidential files or files inside tempplates cannot be accessed