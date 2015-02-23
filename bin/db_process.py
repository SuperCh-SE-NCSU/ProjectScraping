import psycopg2
import sys


def writeDB(username, make, model, year, email):
	con=None
	try:
		con=psycopg2.connect(database='subscribe', user='administrator')
		cur=con.cursor()
		cur.execute("INSERT INTO users VALUES ('" + username + "','" + make + "','" + model + "','" + year + "','" + email + "')")
		con.commit()
		
	except psycopg2.DatabaseError, e:
		print 'Error %s' % e    
		sys.exit(1)
    
	finally:
		if con:
		    con.close()
    
    
def readDB():
    con=None
	try:
		con=psycopg2.connect(database='subscribe', user='administrator')
		cur=con.cursor()
		cur.execute("SELECT * FROM users")
		con.commit()
		
	except psycopg2.DatabaseError, e:
		print 'Error %s' % e    
		sys.exit(1)
    
	finally:
		if con:
		    con.close()
    
