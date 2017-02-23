""" Unit Test for Database Connectivity and Data Abstraction """

import MySQLdb as sql
from os import sys

config = {'host':'104.196.156.219',
           'user':'root',
           'passwd':'bane786',
           'db':'order_processing_app'}

def checkConnection():
    print "Checking connection to mySQL instance"
    db = sql.connect(config['host'], config['user'],config['passwd'],
                     config['db'])
    if db:
        print "Connected to mySQL instance. Host: %s" % (config['host'])
        return True
    else:
        print "Failed to connect to mySQL instance. Host: %s" % (config['host'])
        return False

if __name__ == '__main__':
    
    if checkConnection():
        print "Test 1: checkConnection -- Passed"
    else:
        print "Test 1: checkConnection -- Failed"
        
