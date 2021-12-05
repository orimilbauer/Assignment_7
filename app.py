from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return redirect(url_for('hi'))

@app.route('/info')
def hi():  # put application's code here
    return 'hi' #

@app.route('/try')
def hi2():  # put application's code here
    return redirect('/info')

if __name__ == '__main__':
    app.run()
