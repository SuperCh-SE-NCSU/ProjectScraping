# -*- coding: utf-8 -*-
from collections import namedtuple
import sendgrid
import os
import psycopg2
import urlparse
import datetime,calendar, time
import sched



def perfrom_one_task(task=None):
    now = datetime.datetime.today()
    time_str = now.strftime('%H:%M')
    if time_str > task.time:
        print "Performing", task.name
        task.task()
        time.sleep(86400) # sleep one day to work
        return True
    return False

def run(Tasks):
    while True:
        map(perfrom_one_task, Tasks)
        time.sleep(1)

def sendgridEmail():
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse('postgres://mtnmaytfyidfqd:BogLpswIqI-ZdbcaVTWkRfN3Gh@ec2-107-21-104-188.compute-1.amazonaws.com:5432/d9eedsvtae2kou')

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cur=conn.cursor()
    cur.execute("SELECT * FROM users")
    conn.commit()
    rows = cur.fetchall()

    #send your email here, but that should not public on website, how to solve this problem?
    sg = sendgrid.SendGridClient(os.environ['SENDGRID_USERNAME'], os.environ['SENDGRID_PASSWORD'])
    for row in rows:
        #print row
        #print type(row)
        #print row[0],row[1],row[2],row[3],row[4],row[5]
        username=row[0]
        make=row[1]
        model=row[2]
        year=row[3]
        email=row[4]
        mail_content='<html>'
        mail_content=mail_content+'<p>Dear '+username+',</p>'+'<p>  '+'You want to buy a '+model+' in '+str(year)+'</p>'
        mail_content=mail_content+'</html>'
        message = sendgrid.Mail(to=email, subject='Information from ProjectScraping区分之前的邮件', html=mail_content, text='Body',from_email='ProjectScraping')
        status, msg = sg.send(message)

def sendgridEmailOnce(html_content):
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse('postgres://mtnmaytfyidfqd:BogLpswIqI-ZdbcaVTWkRfN3Gh@ec2-107-21-104-188.compute-1.amazonaws.com:5432/d9eedsvtae2kou')

    conn = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    cur=conn.cursor()
    cur.execute("SELECT * FROM users")
    conn.commit()
    rows = cur.fetchall()

    #send your email here, but that should not public on website, how to solve this problem?
    sg = sendgrid.SendGridClient(os.environ['SENDGRID_USERNAME'], os.environ['SENDGRID_PASSWORD'])

    message = sendgrid.Mail(to='ldong6@ncsu.edu', subject='Information from ProjectScraping区分之前的邮件', html=html_content, text='Body',from_email='ProjectScraping')
    status, msg = sg.send(message)
        
def testSendgridEmail():
    sendgridEmail()

#testSendgridEmail()
#Task=namedtuple('task','name,time,task')
#Tasks = [Task("testtask", "21:28", sendgridEmail)]
#run(Tasks)

