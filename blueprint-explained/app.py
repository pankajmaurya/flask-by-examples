# app.py (main Flask application file)

from flask import Flask
from myblueprint import my_blueprint

app = Flask(__name__)
app.register_blueprint(my_blueprint)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
