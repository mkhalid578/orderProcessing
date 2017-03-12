""" Unit Test for Database Connectivity and Data Abstraction """

from orderProcessDB import EmployInfo, Company, ItemOrder
import unittest

db = EmployInfo()

class TestEmployInfo(unittest.TestCase):

    def test_getPosition(self):
        position = db.getPosition('mkhalid')
        self.assertEqual(position, 'engineer')

    def test_getFirstName(self):
        self.assertEqual(db.getFirstName('mkhalid'), 'muhammed')

    def test_getLastName(self):
        self.assertEqual(db.getLastName('mkhalid'), 'khalid')

    def test_getEmailId(self):
        self.assertEqual(db.getEmailId('mkhalid'), 'mkhalid@uml.edu')

    def test_getPassword(self):
        self.assertEqual(db.getPassword('mkhalid'), 'password')

    def test_getDept(self):
        self.assertEqual(db.getDept('mkhalid'), 'sw')

    def test_getCompanyName(self):
        self.assertEqual(db.getCompanyName('mkhalid'), 'ZOLL')

    def test_getOrderHandler(self):
        self.assertEqual(db.getOrderHandler('mkhalid'), 0)


if __name__ == '__main__':
    unittest.main()


