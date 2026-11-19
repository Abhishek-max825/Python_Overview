from flask import Flask,render_template,request


app = Flask(__name__)

#request.args is used to parse or fetch the query arguments
@app.route("/")
def home():
    name = "Abhi"
    token = 67000
    #this upper values are default one if some one type wrong input at that time it will use this input

    #input giving method : http://localhost:5000/?name=Abhi&token=87000(arguments are passed through the url)

    if "name" in request.args.keys():
        name = request.args['name']

    if "token" in request.args.keys():         
        token = request.args['token']
    return render_template("index.html",name = name, token = token)

app.run(debug=True)