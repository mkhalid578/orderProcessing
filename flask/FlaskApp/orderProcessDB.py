#!/usr/bin/python

import pymysql as sql

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

    def getLastName(self, userId):
        self.cur.execute("SELECT `last-name` FROM employinfo where `user-id`='%s'" % (userId))
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
        self.cur.execute("""INSERT INTO employinfo (`first-name`,`last-name`, `email-id`, `user-id`, `password`,
                            `position`, `department`, `company-name`, `order-handler`)
                            VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%d');"""
                         % (firstName, lastName, email, userId, password, position, department,
                            companyName, orderHandler))
        self.sqlConnection.commit()

    
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
        try:
            self.cur.execute("SELECT name FROM company where name='%s'" % (name))
            row = self.cur.fetchone()
        except TypeError:
            print "Name does not exist"
        else:
            return row[0]

    def getPassword(self, name):
        try:
            self.cur.execute("SELECT password from company where name='%s'" % (name))
            row = self.cur.fetchone()
        except TypeError:
            print "Incorrect Password"
        else:
            return row[0]

    def insert(self, name, password):
        sql = """INSERT INTO `company` (`name`,`password`)
         VALUES ('%s','%s')""" % (str(name), str(password))

        self.cur.execute(sql)
        self.sqlConnection.commit()


class ItemOrder(object):
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

    def getFirstName(self, itemId):
        self.cur.execute("SELECT `first-name` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getLastName(self, itemId):
        self.cur.execute("SELECT `last-name` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getEmailId(self, itemId):
        self.cur.execute("SELECT `email-id` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getPosition(self, itemId):
        self.cur.execute("SELECT `position` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getDepartment(self, itemId):
        self.cur.execute("SELECT `department` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getItemName(self, itemId):
        self.cur.execute("SELECT `item-name` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getItemDetail(self, itemId):
        self.cur.execute("SELECT `item-detail` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getItemQuantity(self, itemId):
        self.cur.execute("SELECT `item-quentities` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getFromWhere(self, itemId):
        self.cur.execute("SELECT `from-where` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getTimePeriod(self, itemId):
        self.cur.execute("SELECT `time-period` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getUseReason(self, itemId):
        self.cur.execute("SELECT `use-reason` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getPlaceOrderDate(self, itemId):
        self.cur.execute("SELECT `place-order-date` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getOrderStatus(self, itemId):
        self.cur.execute("SELECT `order-status` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getShipCompany(self, itemId):
        self.cur.execute("SELECT `shipment-company` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getTrackingNumber(self, itemId):
        self.cur.execute("SELECT `tracking-number` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getTrackingWebsite(self, itemId):
        self.cur.execute("SELECT `tracking-webside` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getExpectedArrival(self, itemId):
        self.cur.execute("SELECT `expected-arriving-date` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getActualArrival(self, itemId):
        self.cur.execute("SELECT `arrived-date` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getComment(self, itemId):
        self.cur.execute("SELECT `comment` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def insert(self,itemId, firstName, lastName, emailId, position, dept, itemName, itemDetail, itemQuantity,
               fromWhere, timePeriod, useReason, placeOrderDate, orderStatus, shipCompany, trackNumber,
               trackingWebsite, expectedArrival, actualArrival, comment):

        sql = """INSERT INTO `item-order` (`item_id`, `first-name`, `last-name`,
                `email-id`, `position`, `department`, `item-name`, `item-detail`,
                `item-quentities`, `from-where`, `time-period`, `use-reason`,
                `place-order-date`, `order-status`, `shipment-company`,
                `tracking-number`, `tracking-webside`, `expected-arriving-date`, `arrived-date`, `comment`)
                 VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%s',
                            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" \
              % (itemId, firstName, lastName, emailId, position, dept, itemName, itemDetail, itemQuantity,
                 fromWhere, timePeriod, useReason, placeOrderDate, orderStatus, shipCompany, trackNumber,
                 trackingWebsite, expectedArrival, actualArrival, comment)

        self.cur.execute(sql)
        self.sqlConnection.commit()

