import os
import psycopg2
import sys
import urlparse

#This file is to write the information we get from users into the database and
#read from database to get the input for crawling functions.

def writeDB(username, make, model, email, minYear, maxYear, minPrice, maxPrice, currentTime):
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	con=None
	try:
		#local db
		#con=psycopg2.connect(database='subscribe', user='administrator')
		#Heroku remote db
		con=psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
		cur=con.cursor()
		cur.execute("INSERT INTO users VALUES ('" + username + "','" + make + "','" + model + "','" + email + "','" + minYear + "','" + maxYear + "','" + minPrice + "','" + maxPrice + "','" + currentTime + "')")
		con.commit()
		
	except psycopg2.DatabaseError, e:
		print 'Error %s' % e    
		sys.exit(1)
    
	finally:
		if con:
		    con.close()
		    
def readDB():
	urlparse.uses_netloc.append("postgres")
	url = urlparse.urlparse(os.environ["DATABASE_URL"])
	con=None
	try:
		#local db
		#con=psycopg2.connect(database='subscribe', user='administrator')
		#Heroku remote db
		con=psycopg2.connect(database=url.path[1:], user=url.username, password=url.password, host=url.hostname, port=url.port)
		cur=con.cursor()
		cur.execute("SELECT * FROM users")
		con.commit()
		
	except psycopg2.DatabaseError, e:
		print 'Error %s' % e    
		sys.exit(1)
    
	finally:
		if con:
		    con.close()
    
