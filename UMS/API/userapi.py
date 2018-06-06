from flask import Flask, render_template
import os
app = Flask(__name__, static_url_path='/static')

userDetails = {'username': 'something', 'password': 'something', 'email': 'abc@gmail.com'}


@app.route('/')
def index():
    return render_template('auth/signin.html')


@app.route('/register')
def login(request):
    user = {'username': request['username'], 'password': request['pwd'], 'email': request['email']}
    return {'msg': 'successful'}


'''send_from_directory(os.path.join(os.getcwd(),'/views/pages'), 'signin.html')'''

if __name__ == "__main__":
    app.run(debug=True)
