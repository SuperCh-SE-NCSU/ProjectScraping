# -*- coding: utf-8 -*-
from collections import namedtuple
import sendgrid
import os
import psycopg2
import urlparse
import datetime,calendar, time
import schedule

def sendgridEmail(html_content,sendtoEmail):
    #send your email here, but that should not public on website, how to solve this problem?
    sg = sendgrid.SendGridClient(os.environ['SENDGRID_USERNAME'], os.environ['SENDGRID_PASSWORD'])
    message = sendgrid.Mail(to=sendtoEmail, subject='Information from VCL@ProjectScraping', html=html_content, text='Body',from_email='ProjectScraping')
    status, msg = sg.send(message)
        
def testSendgridEmail():
    sendgridEmailOnce('123321', 'ldong6@ncsu.edu')

#testSendgridEmail()
#Task=namedtuple('task','name,time,task')
#Tasks = [Task("testtask", "21:13", sendgridEmail('123','zhu6@ncsu.edu'))]
#run(Tasks)

