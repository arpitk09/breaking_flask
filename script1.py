# ! Import Depencies
from flask import Flask

# Create Instance of flask app
app = Flask(__name__)

# Define Route
@app.route("/")

# Content
def home():
    return("Home Page")

#Define 2nd Route and content
@app.route("/about")
def about():
    return("About me")


# Running and controling the script

if (__name__ == "__main__"):
    app.run(debug=True)

