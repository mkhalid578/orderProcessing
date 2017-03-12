import pymysql

config = {
           'host':'104.196.156.219',
           'user':'root',
           'passwd':'bane786',
           'db':'users' }

connection = pymysql.connect(host = config['host'],
                             user = config['user'],
                             password = config['passwd'],
                             db = 'order_processing_app')

if connection:
    print "Success"
else:
    print "Fail"

cursor = connection.cursor()
cursor.execute("SELECT `first-name` FROM employinfo where `user-id`='vibhuti_patel1'")
result = cursor.fetchone()

print result[0]
