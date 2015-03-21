import web
import db_process
import time
import os
#import modelgenerateHtml_development as htmlgen
#This file is to get input information from users,including their name, email
#address, the car they would like to receive information about.(car make,model,
#year of make)
urls = (
  '/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/',base="layout")

class Index(object):
    def GET(self):
        return render.subscribe_form()

    def POST(self):
        currentTime=time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
        form = web.input(username="Nobody", make="Toyota", model="Camry", email="test@ncsu.edu", minYear="2007", maxYear="2015", minPrice="500", maxPrice="100000")        
        #xmlprocess.writeXml("bin/users.xml",form.make,form.model,form.year,form.username,tempcurrentTime,form.email)
        db_process.writeDB(form.username, form.make, form.model, form.email, form.minYear, form.maxYear, form.minPrice, form.maxPrice)
        greeting = "%s, %s, %s, %s, %s, %s, %s, %s" % (form.username, form.make, form.model, form.email, form.minYear, form.maxYear, form.minPrice, form.maxPrice)
        return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()


