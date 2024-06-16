from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/user/<username>')
def user(username):
    return f'Hello, {username}!'


if __name__ == '__main__':
    app.run()
