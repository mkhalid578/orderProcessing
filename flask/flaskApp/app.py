from flask import Flask, render_template, request, session, flash, url_for, redirect
from orderProcessDB import EmployInfo, Company, ItemOrder
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:bane786@104.196.156.219/order_processing_app'
app.config['SECRETY_KEY'] = 'secret'
app.config['TESTING'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

class company(db.Model):
    __tablename__ = 'company'
    name = db.Column(db.String(500), primary_key=True)
    password = db.Column(db.String(12), unique=True)
    def __init__(self, name, password):
        self.name = name
        self.password = password

class employee(db.Model, UserMixin):
    __tablename__ = 'employinfo'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=True)
    last_name = db.Column(db.String(100), unique=True)
    email_id = db.Column(db.String(100), unique=True)
    user_id = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(10), unique=True)
    position = db.Column(db.String(45), unique=True)
    department = db.Column(db.String(100), unique=True)
    company_name = db.Column(db.String(500), unique=True)
    order_authority = db.Column(db.String(200), unique=True)

    def __init__(self, first_name, last_name, email_id, user_id, password, position, department, company_name, order_authority):
        self.first_name = first_name
        self.last_name = last_name
        self.email_id = email_id
        self.user_id = user_id
        self.password = password
        self.position = position
        self.department = department
        self.company_name = company_name
        self.order_authority = order_authority


global_login_user_id = " "
global_company_name = " "


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/compLogin')

@login_manager.user_loader
def load_user(id):
    return employee.query.get(id)

@app.route('/elogin', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        try:
            user = employee.query.filter_by(user_id=str(request.form['username'])).first()
            if request.form['username'] != user.user_id:
                error = 'Invalid Username'
            elif request.form['password'] != user.password:
                error = 'Invalid Password'
            else:
                global global_login_user_id # needed to modify global copy
                global_login_user_id = request.form['username']
                login_user(user)
                return redirect(url_for('placeOrder'))

        except AttributeError:
            error  = 'Invalid Username or Password'

    return render_template('employ-login.html', error=error)

@app.route('/compLogin', methods=['GET', 'POST'])
def companyLogin():
    error = None
    if request.method == 'POST':
        comp = company.query.filter_by(name=str(request.form['CompanyUserId'])).first()
        if request.form['CompanyUserId'] != comp.name:
            error = 'Invalid Company User ID'
        elif request.form['CompanyPassword'] != comp.password:
            error = 'Invalid Password'
        else:
            global global_company_name # needed to modify global copy
            global_company_name = request.form['CompanyUserId']
            return redirect(url_for('login'))
    return render_template('company-login.html', error=error)


@app.route('/processOrder')
@login_required
def placeOrder():
    current = str(current_user.first_name).capitalize()
    return render_template('processing-window.html', current=current)

@app.route('/logout')
@login_required
def UserLogout():
    logout_user()
    message = "You have been logged out"
    return render_template('company-login.html', message=message)


@app.route('/load_profile_data', methods=['GET', 'POST'])
def load_profile_data():
    if current_user:
        firstName = current_user.first_name
        lastName = current_user.last_name
        email = current_user.email_id
        userId = current_user.user_id
        password = str(current_user.password)
        position = current_user.position
        dept = current_user.department
        order_authority = current_user.order_authority
        company = current_user.company_name

       	return json.dumps({'status':'OK', 'firstName':firstName, 'lastName':lastName,
                           'email':email, 'userId':userId, 'password':password, 'position':position,
                           'deptarment':dept, 'company':company ,'order_authority': order_authority})

    else:
        return json.dumps({'status':'NOT-OK'})


@app.route('/load_profile_data_for_form', methods=['GET', 'POST'])
def load_profile_data_for_form():
    if current_user:
        firstName = current_user.first_name
        lastName = current_user.last_name
        email = current_user.email_id
        userId = current_user.user_id
        position = current_user.position
        dept = current_user.department
        company = current_user.company_name

        return json.dumps({'status':'OK', 'firstName':firstName, 'lastName':lastName,
                           'email':email, 'userId':userId, 'position':position,
                           'deptarment':dept, 'company':company })

    else:
        return json.dumps({'status':'NOT-OK'})

@app.route('/load_new_order_data', methods=['GET', 'POST'])
def load_new_order_data():
    new_order_data = request.args.get('key')
    db_new_order_data = json.loads(new_order_data)

    item_order = ItemOrder()
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

    company_name = current_user.company_name
    item_order.insert_new_order(first_name,last_name,email_id,employ,department,item_name,item_detail,
                        item_quentities,from_where,time_period,use_reason,order_status,company_name)

    return "sucessfully added new order in database"

@app.route('/load_edited_profile_data', methods=['GET', 'POST'])
def load_edited_profile_data():
    edited_profile_data = request.args.get('key')
    db_edited_profile_data = json.loads(edited_profile_data)

    user = EmployInfo()
    firstName = db_edited_profile_data['first-name']
    lastName = db_edited_profile_data['last-name']
    email = db_edited_profile_data['email-id']
    userId = db_edited_profile_data['user-id']
    password = db_edited_profile_data['password']
    position = db_edited_profile_data['position']
    dept = db_edited_profile_data['department']
    company = global_company_name
    order_authority = db_edited_profile_data['order-authority']

    user.deleteUser(userId)
    user.insertUser(firstName, lastName, email, userId, password,position,
                  dept,company,order_authority)

    return "sucessfully added edited profile information in database"


@app.route('/data/order-process/orderlist', methods=['GET', 'POST'])
def load_order_data_for_list():
    db = ItemOrder()
    edb = EmployInfo()
    order_authority = current_user.order_authority
    dept = current_user.department
    if order_authority == "employ":
        order_data = db.getOrderListEmp(current_user.company_name, dept)
    else:
        order_data = db.getOrderList(current_user.company_name)

    return json.dumps({'status_data': order_data})

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
    error = None
    if request.method == 'POST':
        try:
            comp_name = str(request.form['id']).strip()
            comp = company.query.filter_by(name=comp_name).first()
            if comp:
                error = 'Company already exists'
            else:
                newComp = company(request.form['id'], request.form['password'])
                db.session.add(newComp)
                db.session.commit()
                return redirect(url_for('companyLogin'))
        except TypeError:
            print 'got an exception'

    return render_template('registerCompany.html', error=error)

@app.route('/registerUser', methods=['GET', 'POST'])
def registerUser():
    error = None
    if request.method == 'POST':
        try:
            enteredUser = str(request.form['userId']).strip()
            user = employee.query.filter_by(user_id=enteredUser).first()
            if user:
                error = "User already exists"
            else:
                firstName = request.form['first']
                lastName = request.form['last']
                email = request.form['email']
                userId = request.form['userId']
                password = request.form['password']
                position = request.form['position']
                dept = request.form['dept']
                company = request.form['company']
                order_authority = 'employ'
                newUser = employee(firstName, lastName, email, userId, password,position,
                                   dept,company,order_authority)
                db.session.add(newUser)
                db.session.commit()
                return redirect(url_for('login'))
        except AttributeError:
            error = "There was a problem registering"

    return render_template('registerUser.html', error=error)

if __name__ == "__main__":
    app.secret_key = 'secret'
    app.run(debug=True)
