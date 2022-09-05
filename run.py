# Importing the Flask class object from the flask library.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/About/')
def about():
    return render_template('about.html')


# If name equals to main, then run the app,
if __name__ == "__main__":
    app.run(debug=True)
