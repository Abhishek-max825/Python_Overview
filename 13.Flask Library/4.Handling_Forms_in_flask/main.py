import os
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])  # in default the form method will be GET only
def form_data_collection():
    if(request.method == "POST"):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file.txt")
        with open(file_path,"w+")as f:
            f.write(f"User name : {request.form['name']}, Email : {request.form['email']}")     
        return render_template("form_handle.html")              
    else:
        return render_template("form_handle.html")

app.run(debug=True)


# Note : 
# This line builds the full path to file.txt in the same folder as main.py:

# __file__ is the path to main.py.
# os.path.abspath(__file__) makes it an absolute path.
# os.path.dirname(...) gets the folder containing main.py.
# os.path.join(..., "file.txt") adds the filename using the correct path separator.