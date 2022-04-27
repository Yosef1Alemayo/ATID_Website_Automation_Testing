from MySQL_Class import DB_Connect

query1 = DB_Connect('localhost', 'root', '******', '3306', 'sakila')

query1.execute('select * from actor where first_name = "KIRK" ')
