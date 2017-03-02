from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = 'mysql://root:bane786@104.196.156.219/order_processing_app'

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Hello flask"


if __name__ == "__main__":
    app.run()
