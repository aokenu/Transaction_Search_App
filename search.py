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

