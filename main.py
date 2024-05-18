
# Import the necessary libraries
from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)

# Define the routes
@app.route("/")
def index():
    """Renders the index page."""
    return render_template("index.html")

@app.route("/tutorials")
def tutorials():
    """Renders the tutorials page."""
    return render_template("tutorials.html")

@app.route("/resources")
def resources():
    """Renders the resources page."""
    return render_template("resources.html")

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
