from flask import Flask
app = Flask(__name__)

userDetails = {'username': 'something', 'password': 'something', 'email': 'abc@gmail.com'}


@app.route('/')
def index():
    return 'Welcome to UMS'


@app.route('/register')
def login(request):
    user = {'username': request['username'], 'password': request['pwd'], 'email': request['email']}
    return {'msg': 'successful'}


if __name__ == "__main__":
    app.run(debug=True)


