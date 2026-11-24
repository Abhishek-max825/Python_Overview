from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
import uuid
import os


UPLOAD_FOLDER = "C:\\Users\\abhis\\OneDrive\\docfiles\\Python Bootcamp - 2025\\14.VidSnapAi\\user_upload"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


app = Flask(__name__)


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create",methods=['GET','POST'])
def create():
    myid = uuid.uuid1() 
    if request.method == "POST":
        print(request.files.keys())
        rec_id = request.form.get("uuid")
        # dec91bdc-e800-11f1-b7a7-106838325962
        desc = request.form.get("text")
        # hello i am abhishek here
        for key,value in request.files.items():
            print(key,value)

            #upload the file 
            file = request.files[key]
            if file :
                filename = secure_filename(file.filename)
                if(not(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],rec_id)))):
                    os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id,filename))


            #capture the discription and store it in file

            with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id,"desc.text"),"w+") as f:
               f.write(desc)


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

# NOTE:
'''

Search for `UPLOAD_FOLDER|secure_filename|rec_id`

These lines handle an uploaded file in the Flask route.

```python
if file:
```

Checks whether a file was actually uploaded. An empty or missing file object is considered false.

```python
filename = secure_filename(file.filename)
```

Cleans the uploaded filename to prevent unsafe characters or paths. For example:

- `../../photo.jpg` becomes `photo.jpg`
- `my photo.jpg` becomes `my_photo.jpg`

This reduces directory-traversal and invalid-filename risks.

```python
if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], rec_id)):
```

- `os.path.join(...)` builds the folder path.
- `os.path.exists(...)` checks whether that folder already exists.
- `not` executes the following block only if the folder is missing.

For example:

```text
C:\Users\abhis\...\14.VidSnapAi\user_upload\<rec_id>
```

```python
os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], rec_id))
```

Creates a folder named after `rec_id`. It acts like a separate upload folder for each recording.

```python
file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, filename))
```

Saves the uploaded file inside that recording folder.

Example final path:

```text
C:\Users\abhis\OneDrive\docfiles\Python Bootcamp - 2025
\14.VidSnapAi\user_upload
\<rec_id>\photo.jpg
```

The complete upload logic is in `main.py`.

For stronger code, validate `rec_id` and use `os.makedirs(..., exist_ok=True)` rather than `os.mkdir(...)`. Otherwise, if `rec_id` contains `..` or `/`, it could create files outside the intended upload directory.
'''
