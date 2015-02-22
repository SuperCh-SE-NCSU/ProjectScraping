import web
import xmlprocess
import time
import os

urls = (
  '/subscribe', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/',base="layout")

class Index(object):
    def GET(self):
        return render.subscribe_form()

    def POST(self):
        form = web.input(username="Nobody", make="Toyota", model="Camry", year="2007",email="test@ncsu.edu")
        tempcurrentTime=time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
        xmlprocess.writeXml("bin/users.xml",form.make,form.model,form.year,form.username,tempcurrentTime,form.email)
        greeting = "%s, %s, %s, %s, %s" % (form.username, form.make,form.model,form.year,form.email)
        return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()
