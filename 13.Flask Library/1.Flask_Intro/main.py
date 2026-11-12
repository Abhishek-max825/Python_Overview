from flask import Flask, render_template  # Import Flask to create the app and render_template to load HTML templates.

app = Flask(__name__)  # Create the Flask application; __name__ helps Flask locate resources such as templates.

@app.route("/")  # Map requests to the site's root URL (/) to the function below.
def hello_world():  # Define the function Flask calls when someone visits /.
    return render_template("index.html")  # Find index.html in the templates folder and return it as the response.

app.run(debug=True)  # Start Flask's development server with debugging and automatic reloading enabled.