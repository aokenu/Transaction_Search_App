import os
from unittest import result
import csv
import datetime
import time
import mysql.connector
import threading
from config import mysql_conn_1, mysql_conn2, mysql_conn3, mysql_conn4
#from mysql.consnector import Error

import smtplib,ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#from datetime import date, timedelta
import time
print("\n\n\n\n")
print("you're about to see the status of your webservices")

#get current time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

#get current date
CurrentDate=datetime.date.today()
days = datetime.timedelta(30)

new_date = CurrentDate - days
final_date= new_date.strftime('%Y-%m-%d')
#%d is for date  
#%m is for month  
#Y is for Year  
print(final_date)
CurrentDate1=datetime.date.today() 
days1 = datetime.timedelta(0)

new_date1 = CurrentDate1 - days1
final_date1= new_date1.strftime('%Y-%m-%d')
print(final_date1)

path1='/Transactions_search/session_ids.csv'
with open(path1, 'r') as file_object:
    lines=file_object.read()
        #print(lines)
    session_ids=lines.split()
    #print(f"' + {banks} + '", sep="','" )
    print(session_ids)
    fieldnames=['session_id','transaction_date','response_code','amount']
    fieldnames4=['session_id','request_time','response_code','amount']
    p=str([str(x) for x in session_ids]).strip("[]")
    print(p)


# Define your queries
postgres_query = "SELECT * FROM mytable"   
mysql_query1 = f"SELECT session_id, transaction_date, response_code, amount FROM nip_report51.`transaction` where session_id in ({p});"
mysql_query2 = f"SELECT session_id, transaction_date, response_code, amount FROM nip_report50.`transaction` where session_id in ({p});"
mysql_query3 = f"SELECT session_id, transaction_date, response_code, amount FROM nip_report47.`transaction` where session_id in ({p});"