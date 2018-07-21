from flask import Flask
from flask import request
from flask import make_response
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    response_string = '<h1>Hello!</h1>'
    response_string += '<p>Your browser is {}</p>'.format(user_agent)
    response = make_response(response_string)
    response.set_cookie('answer','42')
    return response

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

@app.route('/google-it')
def go_away():
    return redirect('http://google.com')
