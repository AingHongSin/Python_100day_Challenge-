import random
import datetime
from flask import Flask, render_template
from api import API


app = Flask(__name__)


@app.route('/')
def home_page():
    current_date = datetime.date.today()
    current_year = current_date.strftime("%Y")
    random_number = random.randint(0,9)
    return render_template("index.html", num=random_number, current_year=current_year)

@app.route('/guess/<name>')
def guess_page(name):
    api = API(name)
    gender = api.gender_request()
    age = api.age_request()
    return render_template("guess.html", name=name.title(), gender=gender, age=age)



if __name__ == '__main__':
    app.run(debug=True)