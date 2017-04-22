from flask import Flask, render_template, request, session, flash, url_for, redirect
from orderProcessDB import EmployInfo, Company, ItemOrder
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
global_company_name = " "

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
            global global_company_name # needed to modify global copy
            global_company_name = request.form['CompanyUserId']

            print request.form['CompanyUserId']
            print request.form['CompanyPassword']
            return redirect(url_for('login'))
    return render_template('company-login.html', error=error)

#@login_required
@app.route('/processOrder')
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
        order_authority = db.getorderAuthority(global_login_user_id)
        company = db.getCompanyName(global_login_user_id)
 
       	return json.dumps({'status':'OK', 'firstName':firstName, 'lastName':lastName,
                       'email':email, 'userId':userId, 'password':password, 'position':position,
                       'deptarment':dept, 'company':company ,'order_authority': order_authority});

    else: 
    		return json.dumps({'status':'NOT-OK'});


@app.route('/load_profile_data_for_form', methods=['GET', 'POST'])
def load_profile_data_for_form():
    db = EmployInfo()
    if global_login_user_id != " ":
    		firstName = db.getFirstName(global_login_user_id)
    		lastName = db.getLastName(global_login_user_id)
    		email = db.getEmailId(global_login_user_id)
    		userId = db.getUserId(global_login_user_id)
    		position = db.getPosition(global_login_user_id)
    		dept = db.getDept(global_login_user_id)
    		company = db.getCompanyName(global_login_user_id)
    
    		return json.dumps({'status':'OK', 'firstName':firstName, 'lastName':lastName,
                       'email':email, 'userId':userId, 'position':position,
                       'deptarment':dept, 'company':company });

    else:
    		return json.dumps({'status':'NOT-OK'});

@app.route('/load_new_order_data', methods=['GET', 'POST'])
def load_new_order_data():
    new_order_data = request.args.get('key')
    db_new_order_data = json.loads(new_order_data)

    db = ItemOrder()
    first_name = db_new_order_data['order-first-name']
    last_name = db_new_order_data['order-last-name']
    email_id = db_new_order_data['order-email-id']
    employ = db_new_order_data['order-employ-position']
    department = db_new_order_data['order-department']
    item_name = db_new_order_data['order-item-name']
    item_detail = db_new_order_data['order-item-detail']
    item_quentities = db_new_order_data['order-item-quentities']
    from_where = db_new_order_data['order-from-where']
    time_period = db_new_order_data['order-time-period']
    use_reason = db_new_order_data['order-use-reason']
    order_status = db_new_order_data['order-status']

    company_name = global_company_name    
    db.insert_new_order(first_name,last_name,email_id,employ,department,item_name,item_detail,
                        item_quentities,from_where,time_period,use_reason,order_status,company_name)

    return "sucessfully added new order in database"

@app.route('/load_edited_profile_data', methods=['GET', 'POST'])
def load_edited_profile_data():
    edited_profile_data = request.args.get('key')
    db_edited_profile_data = json.loads(edited_profile_data)

    db = EmployInfo()
    firstName = db_edited_profile_data['first-name']
    lastName = db_edited_profile_data['last-name']
    email = db_edited_profile_data['email-id']
    userId = db_edited_profile_data['user-id']
    password = db_edited_profile_data['password']
    position = db_edited_profile_data['position']
    dept = db_edited_profile_data['department']
    company = global_company_name
    order_authority = db_edited_profile_data['order-authority']

    db.deleteUser(userId)
    db.insertUser(firstName, lastName, email, userId, password,position,
                          dept,company,order_authority)
    
    return "sucessfully added edited profile information in database"


@app.route('/data/order-process/orderlist', methods=['GET', 'POST'])
def load_order_data_for_list():
    db = ItemOrder()
    edb = EmployInfo()
    order_authority = edb.getorderAuthority(global_login_user_id)
    dept = edb.getDept(global_login_user_id)
    if order_authority == "employ":
        order_data = db.getOrderListEmp(global_company_name, dept)
    else:
        order_data = db.getOrderList(global_company_name)
    return json.dumps({'status_data': order_data}); 

@app.route('/load_deleted_order_data', methods=['GET', 'POST'])
def load_deleted_order_data():
    deleted_order_data = request.args.get('key')
    db_deleted_order_data = json.loads(deleted_order_data)

    db = ItemOrder()
    itemID = db_deleted_order_data['order-item-id']
    db.deleteOrder(itemID)
    return redirect(url_for('load_order_data_for_list'))

@app.route('/load_edited_order_status_data', methods=['GET', 'POST'])
def load_edited_order_status_data():
    edited_order_status_data = request.args.get('key')
    db_edited_order_status_data = json.loads(edited_order_status_data)

    db = ItemOrder()
    itemID = db_edited_order_status_data['order-item-id']
    orderStatus = db_edited_order_status_data['order-status']
    updating_part = db.editOrderStatus(itemID, orderStatus)
    return redirect(url_for('load_order_data_for_list'))

@app.route('/load_edited_order_data', methods=['GET', 'POST'])
def load_edited_order_data():
    edited_order_data = request.args.get('key')
    db_edited_order_data = json.loads(edited_order_data)

    db = ItemOrder()
    itemID = db_edited_order_data['order-item-id']
    orderStatus = db_edited_order_data['order-status']
    orderPlacedDate = db_edited_order_data['placed-order-date']
    shipmentCompany = db_edited_order_data['shipment-company']
    trackingNumber = db_edited_order_data['tracking-number']
    trackingWebsite = db_edited_order_data['tracking-website']
    expectedArrivingDate = db_edited_order_data['expected-arriving-date']
    arrivedDate = db_edited_order_data['arrived-date']
    db.editOrder(itemID, orderStatus, orderPlacedDate, shipmentCompany,
                 trackingNumber, trackingWebsite, expectedArrivingDate, arrivedDate)

    return redirect(url_for('load_order_data_for_list'))


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
            company= global_company_name    
            order_authority = request.form['employ-authority']
            db.insertUser(firstName, lastName, email, userId, password,position,
                          dept,company,order_authority)
            return redirect(url_for('login'))
        else:
            error = "User already exists"
    return render_template('registerUser.html', error=error)

if __name__ == "__main__":
    app.run()
