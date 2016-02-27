import mysql.connector #import oracle's python connector for MySQL
import collections

def _convert(data):
	if isinstance(data, basestring):
		return str(data)
	elif isinstance(data, collections.Mapping):
		return dict(map(_convert, data.iteritems()))
	elif isinstance(data, collections.Iterable):
		return type(data)(map(_convert, data))
	else:
		return data

#Create a class that will give us an object that we can use to connect to a database

class MySQLConnection(object):
	#init method with configurations
	def __init__(self, mydb):
		#begin database configurations
		self.config = {
			'user' : 'root',
			'password' : 'root', 
			'database' : mydb,
			'host' : 'localhost',
			'unix_socket' : '/Applications/MAMP/tmp/mysql/mysql.sock',
		}
		self.conn = mysql.connector.connect(**self.config)

		#fetch function should be used for queries that return multiple rows 
		#rows are returned in a list of tuples with each tuple corresponding to a row

	def fetch(self, query):
		cursor = self.conn.cursor(dictionary=True)
		cursor.execute(query)
		data = list(cursor.fetchall())
		cursor.close()
		return _convert(data)

		#run_mysql_query function should be used for INSERT/UPDATE/DELETE queries
		#it returns the number of rows affected

	def run_mysql_query(self, query):
		cursor = self.conn.cursor(dictionary=True)
		data = cursor.execute(query)
		self.conn.commit()
		cursor.close()
		return data

	#this is the module method to be called by the user in the server.py.. make sure to provide db name
def MySQLConnector(mydb):
	return MySQLConnection(mydb)









