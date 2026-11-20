from flask import Flask, render_template,flash,redirect

app = Flask(__name__)

app.secret_key = "supersecretkey"
# Display one-time messages to users in Flask using the flash function, useful for alerts and notifications.
@app.route("/")
def json():
  return render_template("index.html")

@app.route("/logout")
def logout():
  flash("you have been logged out!","success")
  return redirect("/")

app.run(debug=True)

