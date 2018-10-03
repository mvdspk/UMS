from flask import Flask, render_template
import os
app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('auth/signin.html')


'''send_from_directory(os.path.join(os.getcwd(),'/views/pages'), 'signin.html')'''
if __name__ == "__main__":
    app.run(debug=True,port=8181)
