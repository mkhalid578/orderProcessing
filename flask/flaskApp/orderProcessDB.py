#!/usr/bin/python

import pymysql as sql
import json

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

    def getUserId(self, userId):
        self.cur.execute("SELECT `user_id` FROM employinfo where `user_id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]

    def getPosition(self, userId):
        self.cur.execute("SELECT position FROM employinfo where `user_id` = '%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]

    def getFirstName(self, userId):
        self.cur.execute("SELECT `first_name` FROM employinfo where `user_id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]

    def getLastName(self, userId):
        self.cur.execute("SELECT `last_name` FROM employinfo where `user_id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]


    def getEmailId(self, userId):
        self.cur.execute("SELECT `email_id` FROM employinfo where `user_id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]

    def getPassword(self, userId):
        self.cur.execute("SELECT `password` FROM employinfo where `user_id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]

    def getDept(self, userId):
        self.cur.execute("SELECT `department` FROM employinfo where `user_id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]

    def getCompanyName(self, userId):
        self.cur.execute("SELECT `company_name` FROM employinfo where `user_id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]
    
    def getorderAuthority(self, userId):
        self.cur.execute("SELECT `order_authority` FROM employinfo where `user_id`='%s'" % (userId))
        row = self.cur.fetchone()
        return row[0]

    def insertUser(self, firstName, lastName, email, userId, password,
                       position, department, companyName, order_authority):
        self.cur.execute("""INSERT INTO employinfo (`first_name`,`last_name`, `email_id`, `user_id`, `password`,
                            `position`, `department`, `company_name`, `order_authority`)
                            VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s');"""
                         % (firstName, lastName, email, userId, password, position, department,
                            companyName, order_authority))
        self.sqlConnection.commit()

    def deleteUser(self, userId):
        self.cur.execute("DELETE FROM employinfo where `user_id`='%s'" % (userId))
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
        self.cur.execute("SELECT `first_name` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getLastName(self, itemId):
        self.cur.execute("SELECT `last_name` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getEmailId(self, itemId):
        self.cur.execute("SELECT `email_id` FROM `item-order` where `item_id`='%d'" % (itemId))
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
        self.cur.execute("SELECT `item_name` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getItemDetail(self, itemId):
        self.cur.execute("SELECT `item_detail` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getItemQuantity(self, itemId):
        self.cur.execute("SELECT `item_quentities` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getFromWhere(self, itemId):
        self.cur.execute("SELECT `from_where` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getTimePeriod(self, itemId):
        self.cur.execute("SELECT `time_period` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getUseReason(self, itemId):
        self.cur.execute("SELECT `use_reason` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getPlaceOrderDate(self, itemId):
        self.cur.execute("SELECT `place_order_date` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getOrderStatus(self, itemId):
        self.cur.execute("SELECT `order_status` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getShipCompany(self, itemId):
        self.cur.execute("SELECT `shipment_company` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getTrackingNumber(self, itemId):
        self.cur.execute("SELECT `tracking_number` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getTrackingWebsite(self, itemId):
        self.cur.execute("SELECT `tracking_webside` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getExpectedArrival(self, itemId):
        self.cur.execute("SELECT `expected_arriving_date` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getActualArrival(self, itemId):
        self.cur.execute("SELECT `arrived_date` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def getComment(self, itemId):
        self.cur.execute("SELECT `comment` FROM `item-order` where `item_id`='%d'" % (itemId))
        row = self.cur.fetchone()
        return row[0]

    def editOrderStatus(self, itemID, orderStatus):
        self.cur.execute("UPDATE `item-order` SET `order_status`='%s' where `item_id`='%d'" % (orderStatus,  itemID))
        self.sqlConnection.commit()
        return "True"

    def deleteOrder(self, itemID):
        self.cur.execute("DELETE FROM `item-order` where `item_id`='%d'" % (itemID))
        self.sqlConnection.commit()

    def editOrder(self, itemID, orderStatus, orderPlacedDate, shipmentCompany, trackingNumber,
              trackingWebsite, expectedArrivingDate, arrivedDate):

        self.cur.execute("UPDATE `item-order` SET `order_status`='%s' where `item_id`='%d'" % (orderStatus,  itemID))
        self.cur.execute("UPDATE `item-order` SET `place_order_date`='%s' where `item_id`='%d'" % (orderPlacedDate,  itemID))
        self.cur.execute("UPDATE `item-order` SET `shipment_company`='%s' where `item_id`='%d'" % (shipmentCompany,  itemID))
        self.cur.execute("UPDATE `item-order` SET `tracking_number`='%s' where `item_id`='%d'" % (trackingNumber,  itemID))
        self.cur.execute("UPDATE `item-order` SET `tracking_webside`='%s' where `item_id`='%d'" % (trackingWebsite,  itemID))
        self.cur.execute("UPDATE `item-order` SET `expected_arriving_date`='%s' where `item_id`='%d'" % (expectedArrivingDate,  itemID))
        self.cur.execute("UPDATE `item-order` SET `arrived_date`='%s' where `item_id`='%d'" % (arrivedDate,  itemID))
        self.sqlConnection.commit()

    def getOrderListEmp(self, companyName, dept):
        self.cur.execute("SELECT * FROM `item-order` where `company_name`='%s' AND `department`='%s'" % (companyName, dept))
        row = self.cur.fetchone()
        order_list = []
        while row is not None:
            itemID = row[0]
            firstName = row[1]
            lastName = row[2]
            emailID = row[3]
            position = row[4]
            department = row[5]
            itemName = row[6]
            itemDetail = row[7]
            itemQuentities = row[8]
            fromWhere = row[9]
            timePeriod = row[10]
            useReason = row[11]
            placedOrderDate = row[12]
            orderStatus = row[13]
            shipmentCompany = row[14]
            trackNumber = row[15]
            trackingWebsite = row[16]
            expectedArrivingDate = row[17]
            arrivedDate = row[18]
            order_data = json.dumps({'ItemNumber':itemID, 'First-Name':firstName, 'Last-Name':lastName,
                                     'Email-Id':emailID, 'Position':position, 'Department':department,
                                     'Item-Name':itemName, 'Item-Detail':itemDetail, 'Item-Quentities':itemQuentities,
                                     'From-Where':fromWhere, 'Time-Period':timePeriod, 'Use/Reason':useReason,
                                     'Placed-Order-Date':placedOrderDate, 'Order-Status':orderStatus, 'Shipment-Company':shipmentCompany,
                                     'Tracking-Number':trackNumber, 'Tracking-Webside':trackingWebsite, 
                                     'Expected-Arriving-Date':expectedArrivingDate,'Arrived-Date':arrivedDate}) 
            order_list.append(order_data)
            row = self.cur.fetchone()
        return order_list 

    def getOrderList(self, companyName):
        self.cur.execute("SELECT * FROM `item-order` where `company_name`='%s'" % (companyName))
        row = self.cur.fetchone()
        order_list = []
        while row is not None:
            itemID = row[0]
            firstName = row[1]
            lastName = row[2]
            emailID = row[3]
            position = row[4]
            department = row[5]
            itemName = row[6]
            itemDetail = row[7]
            itemQuentities = row[8]
            fromWhere = row[9]
            timePeriod = row[10]
            useReason = row[11]
            placedOrderDate = row[12]
            orderStatus = row[13]
            shipmentCompany = row[14]
            trackNumber = row[15]
            trackingWebsite = row[16]
            expectedArrivingDate = row[17]
            arrivedDate = row[18]
            order_data = json.dumps({'ItemNumber':itemID, 'First-Name':firstName, 'Last-Name':lastName,
                                     'Email-Id':emailID, 'Position':position, 'Department':department,
                                     'Item-Name':itemName, 'Item-Detail':itemDetail, 'Item-Quentities':itemQuentities,
                                     'From-Where':fromWhere, 'Time-Period':timePeriod, 'Use/Reason':useReason,
                                     'Placed-Order-Date':placedOrderDate, 'Order-Status':orderStatus, 'Shipment-Company':shipmentCompany,
                                     'Tracking-Number':trackNumber, 'Tracking-Webside':trackingWebsite, 
                                     'Expected-Arriving-Date':expectedArrivingDate,'Arrived-Date':arrivedDate}) 
            order_list.append(order_data)
            row = self.cur.fetchone()
        return order_list 

    def insert_new_order(self,firstName, lastName, emailId, position, dept, itemName, itemDetail, itemQuantity,
               fromWhere, timePeriod, useReason, order_status, company_name):

        sql = """INSERT INTO `item-order` (`first_name`, `last_name`,
                `email_id`, `position`, `department`, `item_name`, `item_detail`,
                `item_quentities`, `from_where`, `time_period`, `use_reason`, `order_status`, `company_name`)
                 VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',
                            '%s', '%s', '%s', '%s');""" \
              % (firstName, lastName, emailId, position, dept, itemName, itemDetail, itemQuantity,
                 fromWhere, timePeriod, useReason, order_status, company_name)

        self.cur.execute(sql)
        self.sqlConnection.commit()

    def insert(self,itemId, firstName, lastName, emailId, position, dept, itemName, itemDetail, itemQuantity,
               fromWhere, timePeriod, useReason, placeOrderDate, orderStatus, shipCompany, trackNumber,
               trackingWebsite, expectedArrival, actualArrival, comment):

        sql = """INSERT INTO `item-order` (`item_id`, `first_name`, `last_name`,
                `email_id`, `position`, `department`, `item_name`, `item_detail`,
                `item_quentities`, `from_where`, `time_period`, `use_reason`,
                `place_order_date`, `order_status`, `shipment_company`,
                `tracking_number`, `tracking_webside`, `expected_arriving_date`, `arrived_date`, `comment`)
                 VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',
                            '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');""" \
              % (itemId, firstName, lastName, emailId, position, dept, itemName, itemDetail, itemQuantity,
                 fromWhere, timePeriod, useReason, placeOrderDate, orderStatus, shipCompany, trackNumber,
                 trackingWebsite, expectedArrival, actualArrival, comment)

        self.cur.execute(sql)
        self.sqlConnection.commit()
