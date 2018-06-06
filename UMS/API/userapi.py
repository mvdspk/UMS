from flask import Flask, render_template, request
import os
app = Flask(__name__, static_url_path='/static')

userDetails = {'username': 'something', 'password': 'something', 'email': 'abc@gmail.com'}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('auth/signin.html')
    else:
        return {'msg': 'User logged in successfully'}


@app.route('/register', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/signin.html')
    else:
        user = {'username': request['username'], 'password': request['pwd'], 'email': request['email']}
        return {'msg': 'successfully created the user please login'}


@app.route('/updateuser/<username>', method='PUT')
def updateuser(username):
    if request.body is None:
        return {'error': 'username should not be empty'}
    else:
        '''Integration with Cosmos DB  work in progress'''
        user = {'username': request['username'], 'password': request['pwd'], 'email': request['email']}
        return {'msg': 'updated user'}


@app.route('/deleteuser/<username>', method='DELETE')
def deleteuser(username):
    if request.body is None:
        return {'error': 'username should not be empty'}
    else:
        '''Integration with Cosmos DB  work in progress'''
        return {'msg': 'deleted user'}


'''send_from_directory(os.path.join(os.getcwd(),'/views/pages'), 'signin.html')'''

if __name__ == "__main__":
    app.run(debug=True)
