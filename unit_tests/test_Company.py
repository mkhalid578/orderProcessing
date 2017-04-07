""" Unit Test for Database Connectivity and Data Abstraction """

from orderProcessDB import EmployInfo, Company, ItemOrder
import unittest

db = Company()

class TestEmployInfo(unittest.TestCase):

    def test_getName(self):
        self.assertEqual(db.getName('kronos'), 'kronos')

    def test_getPassword(self):
        self.assertEqual(db.getPassword('kronos'), 'password')

    def test_insert(self):
        try:
            db.insert('chocolate', 'milk')
        except:
            print "Name exists"
        else:
            self.assertEqual(db.getName('chocolate'), 'chocolate')
            self.assertEqual(db.getPassword('chocolate'), 'milk')


if __name__ == '__main__':
    unittest.main()


