import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Add authentication logic here
    # For now, just redirect to the home page
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)


