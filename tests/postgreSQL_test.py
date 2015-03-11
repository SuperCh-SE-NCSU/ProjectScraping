import unittest
import os
import psycopg2
import urlparse
import sys
import testing.postgresql
from sqlalchemy import create_engine

# PostgreSQL server is terminated here
class Testpostgresql(unittest.TestCase):
	def setUp(self):
		#setup new PostgreSQL server
		self.postgresql = testing.postgresql.Postgresql()
		# connect to PostgreSQL
		urlparse.uses_netloc.append("postgres")
		self.url = urlparse.urlparse(os.environ["DATABASE_URL"])
		self.engine = create_engine(self.postgresql.url(self.url))
		self.con = psycopg2.connect(**self.postgresql.dsn())
		self.cur = self.con.cursor()
		self.cur.execute('CREATE TABLE users(username character varying(50),car_make character varying(50),car_model character varying(50),year integer,email character varying(50));')
		self.cur.execute("INSERT INTO users VALUES ('X-zhewei','Toyota','Corolla',2007,'zhu@ncsu.edu');")
		self.con.commit()
        
	def test_addData(self):
		self.cur.execute("INSERT INTO users VALUES ('XX-zhewei','Toyota','Corolla',2007,'zhu@ncsu.edu');")
		self.con.commit()
		self.cur.execute("SELECT COUNT (*) FROM users")
		self.assertEqual(self.cur.fetchall(),[(2L,)])
		self.cur.execute("SELECT * FROM users WHERE username='X-zhewei';")
		self.assertEqual(self.cur.fetchall(),[('X-zhewei','Toyota','Corolla',2007,'zhu@ncsu.edu')])


	def test_deleteData(self):
		self.cur.execute("DELETE FROM users WHERE username='X-zhewei';")
		self.con.commit()
		self.cur.execute("SELECT COUNT (*) FROM users;")
		self.assertEqual(self.cur.fetchall(),[(0L,)])
	
	def test_updateData(self):
		self.cur.execute("UPDATE users SET email='zhewei@ncsu.edu'WHERE username='X-zhewei';")
		self.con.commit()
		self.cur.execute("SELECT email FROM users WHERE username='X-zhewei';")
		self.assertEqual(self.cur.fetchall(),[('zhewei@ncsu.edu',)])

	def tearDown(self):
		self.postgresql.stop()
        
if __name__ == '__main__':
	unittest.main()
