#!/usr/bin/python

import MySQLdb as sql

class EmployInfo(object):
    
    def __init__(self):
        self.user = 'root'
        self.password = 'bane786'
        self.host = '104.196.156.219'
        self.db = 'order_processing_app'
        self.sqlConnection = sql.connect(self.host,
                                         self.user,
                                         self.password,
                                         self.db)
        
        self.cur = self.sqlConnection.cursor()

    def getPosition(self, userId):
        self.cur.execute("SELECT position FROM employinfo where `user-id` = '%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]

    def getFirstName(self, userId):
        self.cur.execute("SELECT `first-name` FROM employinfo where `user-id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]


    def getEmailId(self, userId):
        self.cur.execute("SELECT `email-id` FROM employinfo where `user-id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]
    
    def getPassword(self, userId):
        self.cur.execute("SELECT `password` FROM employinfo where `user-id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]
    
    def getDept(self, userId):
        self.cur.execute("SELECT `department` FROM employinfo where `user-id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]
    
    def getCompanyName(self, userId):
        self.cur.execute("SELECT `company-name` FROM employinfo where `user-id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]
    
    def getOrderHandler(self, userId):
        self.cur.execute("SELECT `order-handler` FROM employinfo where `user-id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]

    def insertUser(self, firstName, lastName, email, userId, password,
                       position, department, companyName, orderHandler):
        self.cur.execute("INSERT INTO employinfo (`first-name`,`last-name`, `email-id`, `user-id`, password, position, department, `company-name`, `order-handler`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%d);" % (firstName, lastName, email, userId, password, position, department, companyName, orderHandler))


    
    def __repr__(self):
        return '[%s, %s]' % (self.host, self.db)


class Company(object):
    
    def __init__(self):
        self.user = 'root'
        self.password = 'bane786'
        self.host = '104.196.156.219'
        self.db = 'order_processing_app'
        self.sqlConnection = sql.connect(self.host,
                                         self.user,
                                         self.password,
                                         self.db)
        
        self.cur = self.sqlConnection.cursor()

    def getName(self, name):
        row = self.cur.execute("SELECT name FROM company where name='%s'" % (name))
        return row

    def getPassword(self, name):
        row = self.cur.execute("SELECT password from company where name='%s'" % (name))
        return row

    def insert(self, name, password):
        sql = """INSERT INTO company(name,password)
         VALUES (%s,%s)""", (name, password)
        
        self.cur.execute(sql)
        
