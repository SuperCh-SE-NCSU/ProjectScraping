import urllib2
import re
import time
import xml.etree.ElementTree as ET
#This file is to crawl craigslit to get car sale information
#and send emails to users

tree = ET.parse('country_data.xml')
root = tree.getroot()

model=list()
price=list()
carlink=list()
abstractInformation=list()
timePost=list()
today=True
num=0
#print time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))
mystrTime=time.strftime('%Y-%m-%d %X',time.localtime(time.time()))

for user in root.findall('user'):
    temp=user.find('lastvisitTime')
    lastvisitTime=temp.text
    #print temp.text
    temp.text=mystrTime
    #print user.find('lastvisitTime').text

while today:
    if num==0:
        tempstr='http://raleigh.craigslist.org/search/cto//'
    else:
        tempstr='http://raleigh.craigslist.org/search/cto?s='+str(num)+'//'
    
    response = urllib2.urlopen(tempstr)
    html = response.read()

    Terms8=re.findall(r'<span class="txt"> <span class="star"></span> <span class="pl"> <time\s*datetime=".+?" title=".+?">.+?</time> <a href=".+?"\s*data-id="\w+"\s*class="\w+">.+?</a>\s*</span>\s*<span\s*class="l2"> .+?</p>',html)
    if not Terms8:
        break
    for i in range(len(Terms8)):
        timeCur=re.search(r'<time\s*datetime="(.+?)" title="(.+?)">(.+?)</time> <a href="(.+?)"\s*data-id="(\w+)"\s*class="(\w+)">(.+?)</a>\s*</span>\s*<span\s*class="l2">\s*<span\s*?class="price">&#x0024;(\w+?)</span>',Terms8[i])
        if timeCur:
            #print lastvisitTime
            #print timeCur.group(1)
            if timeCur.group(1)<=lastvisitTime:
                today=False
                break
            if (('corolla' in timeCur.group(7).lower()) and (int(timeCur.group(8))>6000)):
                timePost.append(timeCur.group(3))
                price.append(timeCur.group(8))
                carlink.append(timeCur.group(4))
                abstractInformation.append(timeCur.group(7))
                print timeCur.group(1)
                print timeCur.group(2)
                print timeCur.group(3)
                print timeCur.group(4)
                print timeCur.group(5)
                print timeCur.group(6)
                print timeCur.group(7)
                print timeCur.group(8)    
        
    print num    
    num=num+100
    print '------------------------------'

#coding: utf-8 
import smtplib 
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from email.mime.audio import MIMEAudio 
from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart 

import os, mimetypes 

username = 'dragonfly90mad@gmail.com' # ÓûﾧÃû 
password = '********' # ÃÜÂë 

sender = 'dragonfly90mad@gmail.com' # ﾷﾢﾼþÈËÓÊÏä 
receiver = 'zhu6@ncsu.edu' # ÊռþÈËÓÊÏä 
subject = 'python email test'
mail_content='<html>'
for i in range(len(timePost)):
    mail_content =mail_content+'<p>'+timePost[i]+' , '+price[i]+' dollars,  '+abstractInformation[i]+',  <a href="http://raleigh.craigslist.org'+carlink[i]+'">http://raleigh.craigslist.org'+carlink[i]+'</a></p>' # emailÄÚÈÝ 
mail_content=mail_content+'</html>'
msgText = MIMEText(mail_content,'html','utf-8') 

msg = MIMEMultipart() 
msg['Subject'] = subject 
msg.attach(msgText) 

filepath = unicode('NCSU.png','utf8') 
ctype, encoding = mimetypes.guess_type(filepath) 
if ctype is None or encoding is not None: 
    ctype = "application/octet-stream" 
maintype, subtype = ctype.split("/", 1) 

if maintype == 'text': 
    fp = open(filepath) 
    attachment = MIMEText(fp.read(), _subtype=subtype) 
    fp.close() 
elif maintype == 'image': 
    fp = open(filepath, 'rb') 
    attachment = MIMEImage(fp.read(), _subtype=subtype) 
    fp.close() 
elif maintype == 'audio': 
    fp = open(filepath, 'rb') 
    attachment = MIMEAudio(fp.read(), _subtype=subtype) 
    fp.close() 
else: 
    fp = open(filepath, 'rb') 
    attachment = MIMEBase(maintype, subtype) 
    attachment.set_payload(fp.read()) 
    fp.close() 
    encoders.encode_base64(attachment) 
attachment.add_header('Content-Disposition', 'attachment', filepath=filepath) 
#msg.attach(attachment) 
#don't use attachment
mail_server = 'smtp.gmail.com' 
mail_server_port = 587 
server = smtplib.SMTP(mail_server, mail_server_port) 
# server.set_debuglevel(1) # ﾵ÷ÊÔģʽ 
server.ehlo() 
server.starttls() 
server.login(username, password) 
server.sendmail(sender, receiver, msg.as_string()) 
server.quit()
               
