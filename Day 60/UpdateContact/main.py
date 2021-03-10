from flask import Flask, render_template, request
import requests
import emailSending

posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)


title = "Successfully sent message"

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/contact', methods=('GET', 'POST'))
def contact():
    if request.method == "POST":
        print(request.form['Name'])
        print(request.form['Email-Address'])
        print(request.form['Phone-Number'])
        print(request.form['Message'])
        emailSending.sending(name=request.form['Name'], email=request.form['Email-Address'], phoneNumber=request.form['Phone-Number'], message=request.form['Message'])
        return  render_template('contact.html', sent=True)
    return render_template('contact.html', sent=False)





if __name__ == "__main__":
    app.run(debug=True)
