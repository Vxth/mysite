
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Jerrey Moss(The Goat)!'

@app.route('/about_me')
def about_me():
    return app.send_static_file('about_me.html')


@app.route('/Class_Schedule')
def Class_Schedule():
    return app.send_static_file('Class_Schedule.html')

@app.route('/Register')
def Register():
    return app.send_static_file('class_ schedule.html')