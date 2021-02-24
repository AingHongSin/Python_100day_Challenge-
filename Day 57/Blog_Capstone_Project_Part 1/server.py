from flask import Flask, render_template
from post import Post

post = Post()

app = Flask(__name__)

@app.route('/')
def home():
    data = post.request_post()
    return render_template("index.html", post=data)

@app.route('/post/<id>')
def get_post(id):
    data = post.request_post()
    return render_template("post.html", id=int(id), post=data)

if __name__ == "__main__":
    app.run(debug=True)
