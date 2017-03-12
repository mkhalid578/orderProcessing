from flask import Flask, render_template, request, session, flash, url_for, redirect
from orderProcessDB import EmployInfo, Company

app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/elogin', methods=['GET', 'POST'])
def login():
    db = EmployInfo()
    error = None
    if request.method == 'POST':
        try:
            if request.form['username'] != db.getFirstName(request.form['username']):
                error = 'Invalid Username'
            elif request.form['password'] != db.getPassword(request.form['username']):
                error = 'Invalid Password'
        except TypeError:
            print "Combination of Username and Password do not exist"
            error = "Username and/ or Password are incorrect"
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
        try:
            if request.form['CompanyUserId'] != db.getName(request.form['CompanyUserId']):
                error = 'Invalid Company User ID'
            elif request.form['CompanyPassword'] != db.getPassword(request.form['CompanyUserId']):
                error = 'Invalid Password'
        except TypeError:
            print "Invalid Company ID or Invalid Password"
            error = "Invalid Company ID or Invalid Password"
        else:
            print request.form['CompanyUserId']
            print request.form['CompanyPasswordls']
            return redirect(url_for('login'))
    return render_template('company-login.html', error=error)

@app.route('/processOrder')
def placeOrder():
    return render_template('processing-window.html')

if __name__ == "__main__":
    app.run()
