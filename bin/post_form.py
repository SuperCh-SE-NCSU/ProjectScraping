import web
import db_process
import time
import os
#This file is to get input information from users,including their name, email
#address, the car they would like to receive information about.(car make,model,
#year of make)
urls = (
  '/', 'Index',
  '/carInformation','Information'
)

app = web.application(urls, globals())

render = web.template.render('templates/',base="layout")

render2=web.template.render('templates/')

class Index(object):
    def GET(self):
        return render.subscribe_form()

    def POST(self):
        form = web.input(username="Nobody", make="Toyota", model="Camry", year="2007",email="test@ncsu.edu")
        tempcurrentTime=time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
        #xmlprocess.writeXml("bin/users.xml",form.make,form.model,form.year,form.username,tempcurrentTime,form.email)
        db_process.writeDB(form.username, form.make, form.model, form.year, form.email)
        greeting = "%s, %s, %s, %s, %s" % (form.username, form.make,form.model,form.year,form.email)
        return render.index(greeting = greeting)

class Information(object):
    def GET(self):
        return render2.carInformation()

    def POST(self):
        form = web.input(username="Nobody", make="Toyota", model="Camry", year="2007",email="test@ncsu.edu")
        greeting = "%s, %s, %s, %s, %s" % (form.username,form.make,form.model,form.year,form.email)
        return render.index(greeting = greeting)
        
if __name__ == "__main__":
	app.run()


