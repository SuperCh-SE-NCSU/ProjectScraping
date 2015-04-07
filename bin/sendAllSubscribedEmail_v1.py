# -*- coding: utf-8 -*-
import sendgrid
import os
import psycopg2
import urlparse
import datetime,calendar, time
import schedule
import db_process as db
import sendEmail_v1 as sendEmail
import modelgenerateHtml_development as htmlgen


def sendAllSubscribedEmail():
    #read DB records
    rows = db.readDB()
    for row in rows:
        make=row[1]
        model=row[2]
        email=row[3]
        #year should be string, but in DB year is integer
        startyear=str(row[4])
        endyear=str(row[5])
        minPrice=row[6]
        maxPrice=row[7]
        ctime=row[8]
        print make,model,startyear,endyear,minPrice,maxPrice,ctime
        #print type(make),type(model),type(startyear),type(endyear),type(minPrice),type(maxPrice),type(time)
        html=htmlgen.generateHTML(make,model,startyear,endyear,minPrice,maxPrice,(datetime.datetime.now()-datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M:%S"))
        print email
        sendEmail.sendgridEmail(html, email)

schedule.every(60).minutes.do(sendAllSubscribedEmail)
while True:
    schedule.run_pending()
