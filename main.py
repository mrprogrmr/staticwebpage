from flask import Flask, render_template
from data_science import Data_Science

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/projects')
def show_projects():
    return render_template('projects.html')



if __name__ == "__main__":
    app.run(debug=True)
