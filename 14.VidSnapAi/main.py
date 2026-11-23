from flask import Flask, render_template,request
import uuid
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create",methods=['GET','POST'])
def create():
    myid = uuid.uuid1() 
    if request.method == "POST":
        print(request.files.keys())
        for key,value in request.files.items():
            print(key,value)

    return render_template("create.html",myid=myid)

#output : hitting to the back end points with files
# and there is one more thing uuid  is a library that creates unique id 
# dict_keys(['file1', 'file2', 'file3', 'file4'])
# file1 <FileStorage: '1.jpg' ('image/jpeg')>
# file2 <FileStorage: '2.jpg' ('image/jpeg')>
# file3 <FileStorage: '3.jpg' ('image/jpeg')>
# file4 <FileStorage: '' ('application/octet-stream')>

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)