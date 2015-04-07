# -*- coding: utf-8 -*-
import sendgrid
import os
import datetime,time


def sendgridEmail(html_content,sendtoEmail):
    #send your email here, but that should not public on website, how to solve this problem?
    sg = sendgrid.SendGridClient(os.environ['SENDGRID_USERNAME'], os.environ['SENDGRID_PASSWORD'])
    message = sendgrid.Mail(to=sendtoEmail, subject='Information from VCL@ProjectScraping', html=html_content, text='Body',from_email='ProjectScraping')
    msg = sg.send(message)
        
def testSendgridEmail():
    sendgridEmail(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'zhu6@ncsu.edu')

#testSendgridEmail()
#schedule.every().day.at((datetime.datetime.now()+datetime.timedelta(minutes=1)).strftime("%H:%M")).do(sendgridEmail(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'zhu6@ncsu.edu'))
#while True:
#    schedule.run_pending()




