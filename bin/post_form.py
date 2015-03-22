import web
import db_process
import time
import os
import sendEmail_v1 as sendEmail
import modelgenerateHtml_development as htmlgen
from multiprocessing import Process
#import modelgenerateHtml_development as htmlgen
#This file is to get input information from users,including their name, email
#address, the car they would like to receive information about.(car make,model,
#year of make)
def f(make,model,startyear,endyear,minPrice,maxPrice,time):
    html=htmlgen.generateHTML(make,model,startyear,endyear,minPrice,maxPrice,time)
    print html
    sendEmail.sendgridEmailOnce(html)
    
    
urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/',base="layout")

class Index(object):
    def GET(self):
        return render.subscribe_form()

    def POST(self):
        tempcurrentTime=time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
        form = web.input(username="Nobody", make="Toyota", model="Camry", email="test@ncsu.edu", minYear="2007", maxYear="2015", minPrice="500", maxPrice="100000", currentTime=tempcurrentTime)        
        #xmlprocess.writeXml("bin/users.xml",form.make,form.model,form.year,form.username,tempcurrentTime,form.email)
        db_process.writeDB(form.username, form.make, form.model, form.email, form.minYear, form.maxYear, form.minPrice, form.maxPrice, form.currentTime)
        p = Process(target=f, args=(form.make,form.model,form.minYear,form.maxYear,int(form.minPrice),int(form.maxPrice),'2015-03-06 23:40:13'))
        p.start()
        greeting = "%s, %s, %s, %s, %s, %s, %s, %s \n Please wait for ProjectScraping Email" % (form.username, form.make, form.model, form.email, form.minYear, form.maxYear, form.minPrice, form.maxPrice)
        return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()


