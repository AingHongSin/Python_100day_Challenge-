import requests
from flask import Flask, render_template
app = Flask(__name__)

responses = requests.get(url="https://api.npoint.io/43644ec4f0013682fc0d")
data = responses.json()





@app.route('/')
def home():
    return render_template('index.html', data_post=data)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post/<id>")
def post(id):
    return render_template('post.html', id=int(id), data_post=data)


if __name__ == '__main__':
    app.run(debug=True)