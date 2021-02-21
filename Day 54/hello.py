from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/bye')
def sey_goodbye():
    return 'Good Bye'
    

if __name__ == '__main__':
    app.run()