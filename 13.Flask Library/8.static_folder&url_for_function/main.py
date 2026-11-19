from flask import Flask, render_template
'''Customize the static folder location and use the url_for function to generate dynamic URLs for static files in Flas'''

# app = Flask(__name__,static_url_path="/public")
#http://127.0.0.1:5000/public/style.css here we are using public instead of static, in here we are just alternating the url path
# this is how we changing the static url path

# app = Flask(__name__,static_folder="assets") #dont use / here because its an absolute path 
# http://127.0.0.1:5000/assets/anotherstyle.css this is how we changing static folder path

app = Flask(__name__,static_folder="assets",static_url_path="/public")
@app.route("/")
def home():
    return render_template("index.html")

app.run(debug=True)