""" Unit Test for Database Connectivity and Data Abstraction """

from orderProcessDB import EmployInfo, Company, ItemOrder
from datetime import datetime
import unittest

db = ItemOrder()

class TestEmployInfo(unittest.TestCase):

    def test_getFirstName(self):
        self.assertEqual(db.getFirstName(1), 'muhammed')

    def test_getLastName(self):
        self.assertEqual(db.getLastName(1), 'khalid')

    def test_getEmailId(self):
        self.assertEqual(db.getEmailId(1), 'mkhalid@gmail.com')

    def test_getDept(self):
        self.assertEqual(db.getDepartment(1), 'sw')

    def test_getPosition(self):
        self.assertEqual(db.getPosition(1), 'engineer')

    def test_getItemName(self):
        self.assertEqual(db.getItemName(1), 'printer')

    def test_getItemDetail(self):
        self.assertEqual(db.getItemDetail(1), 'HP Printer')

    def test_getItemQuantity(self):
        self.assertEqual(db.getItemQuantity(1), 1)

    def test_getFromWhere(self):
        self.assertEqual(db.getFromWhere(1), 'HP')

    def test_getTimePeriod(self):
        self.assertEqual(db.getTimePeriod(1), '2017-03-12 12:41:42')

    def test_getUseReason(self):
        self.assertEqual(db.getUseReason(1), 'i want to print stuff')

    def test_getPlaceOrderDate(self):
        self.assertEqual(db.getPlaceOrderDate(1), datetime(2017,3,12,12,41,42))

    def test_getOrderStatus(self):
        self.assertEqual(db.getOrderStatus(1), 'Pending Approval')

    def test_getShipCompany(self):
        self.assertEqual(db.getShipCompany(1), 'UPS')

    def test_getTrackNumber(self):
        self.assertEqual(db.getTrackingNumber(1), '1DEF342223FFDE')

    def test_getTrackWebsite(self):
        self.assertEqual(db.getTrackingWebsite(1), 'www.ups.com')

    def test_getExpectedArrival(self):
        self.assertEqual(db.getExpectedArrival(1),datetime(2017,3,12,12,41,42))

    def test_getActualArrival(self):
        self.assertEqual(db.getActualArrival(1), datetime(2017,3,12,12,41,42))

    def test_getComment(self):
        self.assertEqual(db.getComment(1), None)

    def test_insert(self):
        db.insert(5, 'joe','king','jk@google.com','engineer','sw','Phone','Apple iPhone',1,'Apple',
                  'May 2018','Need new cellphone','2017-03-12 12:41:42','Pending Approval','UPS','DFDFADF1343DFDF',
                  'www.ups.com','2017-03-12 12:41:42','2017-03-12 12:41:42', 'need ASAP')

        self.assertEqual(db.getFirstName(5), 'joe')
        self.assertEqual(db.getLastName(5), 'king')
        self.assertEqual(db.getEmailId(5), 'jk@google.com')
        self.assertEqual(db.getDepartment(5), 'sw')
        self.assertEqual(db.getPosition(5), 'engineer')
        self.assertEqual(db.getItemName(5), 'Phone')
        self.assertEqual(db.getItemDetail(5), 'Apple iPhone')
        self.assertEqual(db.getItemQuantity(5), 1)
        self.assertEqual(db.getFromWhere(5), 'Apple')
        self.assertEqual(db.getTimePeriod(5), 'May 2018')
        self.assertEqual(db.getUseReason(5), 'Need new cellphone')
        self.assertEqual(db.getPlaceOrderDate(5), datetime(2017,3,12,12,41,42))
        self.assertEqual(db.getOrderStatus(5), 'Pending Approval')
        self.assertEqual(db.getShipCompany(5), 'UPS')
        self.assertEqual(db.getTrackingNumber(5), 'DFDFADF1343DFDF')
        self.assertEqual(db.getTrackingWebsite(5), 'www.ups.com')
        self.assertEqual(db.getExpectedArrival(5), datetime(2017,3,12,12,41,42))
        self.assertEqual(db.getActualArrival(5), datetime(2017,3,12,12,41,42))
        self.assertEqual(db.getComment(5), 'need ASAP')


if __name__ == '__main__':
    unittest.main()


