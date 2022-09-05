# Importing the Flask class object from the flask library.
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Home Page"


@app.route('/About/')
def about():
    return "About content ...!"


# If name equals to main, then run the app,
if __name__ == "__main__":
    app.run(debug=True)
