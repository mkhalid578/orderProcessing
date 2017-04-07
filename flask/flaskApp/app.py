from flask import Flask, render_template, request, session, flash, url_for, redirect
from orderProcessDB import EmployInfo, Company
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)


@app.route('/elogin', methods=['GET', 'POST'])
def login():
    db = EmployInfo()
    error = None
    if request.method == 'POST':
        if request.form['username'] != db.getUserId(request.form['username']):
            error = 'Invalid Username'
        elif request.form['password'] != str(db.getPassword(request.form['username'])):
            error = 'Invalid Password'
        else:
            print request.form['username']
            print request.form['password']
            return redirect(url_for('placeOrder'))
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
def placeOrder():
    return render_template('processing-window.html')

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
