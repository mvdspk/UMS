from flask import Flask, request, send_from_directory
import os
app = Flask(__name__)

userDetails = {'username': 'something', 'password': 'something', 'email': 'abc@gmail.com'}


@app.route('/')
def index():
    path=os.path.join(os.getcwd(),'views','pages')
    return send_from_directory(path, 'signin.html')


@app.route('/register')
def login(request):
    user = {'username': request['username'], 'password': request['pwd'], 'email': request['email']}
    return {'msg': 'successful'}


if __name__ == "__main__":
    app.run(debug=True)


