import os
from unittest import result 
import csv
import datetime
import time
import mysql.consnector
import threading
from config import mysql_conn, mysql_connv
#from mysql.connector import Error 


import smtplib,ssl
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


#from datetime import date, timedelta
import time
pr
int("\n\n\n\n")
print("you're about to see the status of your webservices")
#get current time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)


#get cureent date
CurrentDate=datetime.date.today()  
days = datetime.timedelta(30)

