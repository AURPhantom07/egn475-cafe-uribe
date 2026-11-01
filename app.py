# Importing from Flask
from flask import Flask

# Creating the Flask app object
app = Flask(__name__)

# Creates the "Lobby" or "Main" page of the website
@app.route("/")
def home():
    return "Hello Flask. I DO understand how Flask works."

# Creates the "About" page of the website, that can be accessed via the "/about" URL
@app.route("/about")
def about():
    return "Café Calle Ocho is a cafe in Little Havana."
