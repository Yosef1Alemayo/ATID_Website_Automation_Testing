from mySql import DB_Connect

''' This Query is for example, There is no DataBase in The Website .. 
 The Website is for Practice To QA '''

query1 = DB_Connect('localhost', 'root', '******', '3306', 'sakila')

query1.execute('select * from actor where first_name = "KIRK" ')
