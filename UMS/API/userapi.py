from flask import Flask, request, send_from_directory
import os
app = Flask(__name__)


@app.route('/')
def index():
    path=os.path.join(os.getcwd(),'views','pages')
    return send_from_directory(path, 'signin.html')


if __name__ == "__main__":
    app.run(debug=True)


