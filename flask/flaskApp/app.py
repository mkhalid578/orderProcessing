from flask import Flask, render_template, request, session, flash, url_for, redirect
from orderProcessDB import EmployInfo, Company
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:bane786@104.196.156.219/order_processing_app'
app.config['SECRETY_KEY'] = 'secret'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class company(db.Model):
    __tablename__ = 'company'
    name = db.Column(db.String(500), primary_key=True)
    password = db.Column(db.String(12), unique=True)

class employee(db.Model):
    __tablename__ = 'employinfo'
    first_name = db.Column(db.String(100), unique=True)
    last_name = db.Column(db.String(100), unique=True)
    email_id = db.Column(db.String(100), unique=True)
    user_id = db.Column(db.String(45), primary_key=True)
    password = db.Column(db.String(10), unique=True)
    position = db.Column(db.String(45), unique=True)
    department = db.Column(db.String(100), unique=True)
    company_name = db.Column(db.String(500), unique=True)
    order_authority = db.Column(db.String(200), unique=True)



global_login_user_id = " "

@app.route('/elogin', methods=['GET', 'POST'])
def login():
    db = EmployInfo()
    error = None
    if request.method == 'POST':
        try:
            if request.form['username'] != db.getUserId(request.form['username']):
                error = 'Invalid Username'
            elif request.form['password'] != str(db.getPassword(request.form['username'])):
                error = 'Invalid Password'
            else:
                global global_login_user_id # needed to modify global copy
                global_login_user_id = request.form['username']

                print request.form['username']
                print request.form['password']

                return redirect(url_for('placeOrder'))

        except TypeError:
            error  = 'Invalid Username or Password'

    return render_template('employ-login.html', error=error)

@app.route('/compLogin', methods=['GET', 'POST'])
def companyLogin():
    db = Company()
    error = None
    if request.method == 'POST':
        if request.form['CompanyUserId'] != db.getName(request.form['CompanyUserId']):
            error = 'Invalid Company User ID'
        elif request.form['CompanyPassword'] != db.getPassword(request.form['CompanyUserId']):
            error = 'Invalid Password'
        else:
            print request.form['CompanyUserId']
            print request.form['CompanyPassword']
            return redirect(url_for('login'))
    return render_template('company-login.html', error=error)

@app.route('/processOrder')
@login_required
def placeOrder():
    return render_template('processing-window.html')

@app.route('/compLogin')
def UserLogout():
    return render_template('company-login.html')


@app.route('/load_profile_data', methods=['GET', 'POST'])
def load_profile_data():
    db = EmployInfo()
    if global_login_user_id != " ":
    		firstName = db.getFirstName(global_login_user_id)
    		lastName = db.getLastName(global_login_user_id)
    		email = db.getEmailId(global_login_user_id)
    		userId = db.getUserId(global_login_user_id)
    		password = str(db.getPassword(global_login_user_id))
    		position = db.getPosition(global_login_user_id)
    		dept = db.getDept(global_login_user_id)
    		company = db.getCompanyName(global_login_user_id)
    		#orderHandler = db.getOrderHandler(global_login_user_id)
    		orderHandler = 1

    		return json.dumps({'status':'OK', 'firstName':firstName, 'lastName':lastName,
                       'email':email, 'userId':userId, 'password':password, 'position':position,
                       'deptarment':dept, 'company':company ,'orderHandler':orderHandler});

    else:
    		return json.dumps({'status':'NOT-OK'});

@app.route('/update_profile_data', methods=['GET', 'POST'])
def update_profile_data():
    return "hi"




@app.route('/registerCompany', methods=['GET', 'POST'])
def registerCompany():
    db = Company()
    error = None
    if request.method == 'POST':
        try:
            if request.form['id'] != db.getName(request.form['id']):
                pass
        except TypeError: # When this exception raised, it is safe to say the company does not exist
            db.insert(request.form['id'], request.form['password'])
            error = "Company added successfully"
            return redirect(url_for('companyLogin'))
        else:
            error = "Company Already exists"

    return render_template('registerCompany.html', error=error)

@app.route('/registerUser', methods=['GET', 'POST'])
def registerUser():
    db = EmployInfo()
    error = None
    if request.method == 'POST':
        try:
            if request.form['userId'] != db.getUserId(request.form['userId']):
                pass
        except TypeError:
            firstName = request.form['first']
            lastName = request.form['last']
            email = request.form['email']
            userId = request.form['userId']
            password = request.form['password']
            position = request.form['position']
            dept = request.form['dept']
            company = request.form['company']
            orderHandler = int(request.form['orderHandler'])
            db.insertUser(firstName, lastName, email, userId, password,position,
                          dept,company,orderHandler)
            return redirect(url_for('login'))
        else:
            error = "User already exists"
    return render_template('registerUser.html', error=error)

if __name__ == "__main__":
    app.run()
