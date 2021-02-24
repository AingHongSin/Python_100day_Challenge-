import random
import datetime
from flask import Flask, render_template
import api


app = Flask(__name__)


@app.route('/')
def home_page():
    current_date = datetime.date.today()
    current_year = current_date.strftime("%Y")
    random_number = random.randint(0,9)
    return render_template("index.html", num=random_number, current_year=current_year)

@app.route('/guess/<name>')
def guess_page(name):
    gender = api.gender_request(name)
    age = api.age_request(name)
    return render_template("guess.html", name=name.title(), gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    post = api.blog_request()
    return render_template('blog.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)