from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return "<em>" + function() + "</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return "<u>" + function() + "</u>"
    return wrapper_function

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is paragraph</p>' \
           '<img src="https://media.giphy.com/media/xTiTnf9SCIVk8HIvE4/giphy.gif" width=200>'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def sey_goodbye():
    return 'Good Bye'

@app.route('/<name>/<int:number>')
def greet(name, number):
    return f"Hello there {name}, you are {number} year old!"

if __name__ == '__main__':
    app.run(debug=True)