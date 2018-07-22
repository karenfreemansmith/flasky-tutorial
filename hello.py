from flask import Flask, render_template
from flask import request, make_response, redirect
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/google-it')
def go_away():
    return redirect('http://google.com')

@app.route('/cookie')
def cookie():
    user_agent = request.headers.get('User-Agent')
    response_string = '<h1>Hello!</h1>'
    response_string += '<p>Your browser is {}</p>'.format(user_agent)
    response = make_response(response_string)
    response.set_cookie('answer','42')
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
