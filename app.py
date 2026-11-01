# Importing from Flask
from flask import Flask

# Creating the Flask application object
app = Flask(__name__)

# Creates the "Lobby" or "Main" page of the website
@app.route("/")
def home():
    return "Welcome to Café Calle Ocho."

# Creates the "About" page of the website, that can be accessed via the "/about" URL
@app.route("/about")
def about():
    return "Café Calle Ocho is a cafe in Little Havana."
