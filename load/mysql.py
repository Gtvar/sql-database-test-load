from __future__ import print_function
from datetime import date, datetime, timedelta
import pymysql
import names
from faker import Faker

def addUsers( conn ) :
    cur = conn.cursor()

    cur.execute("INSERT INTO `users` (`name`, `birth_date`, `created_at`) VALUES (%s, %s, NOW())",
        (names.get_first_name(), fake.date_between(start_date='-30y', end_date='today')))

    conn.commit()

myConnection = pymysql.connect( host='localhost', user='root', passwd='root', db='yk' )
fake = Faker()

n = 10000000
while n > 0:
    n -= 1
    addUsers( myConnection )

myConnection.close()
