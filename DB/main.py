from mySql import DB_Connect

''' This Query is for example, There is no DataBase in The Website .. 
 The Website is for Practice To QA '''


class Main_Queries:
    connect = DB_Connect('localhost', 'root', 'yossi2611', '3306', 'sakila')

    @staticmethod
    def query1():
        a = Main_Queries.connect.execute('select * from actor where first_name = "KIRK" ')
        return type(a)





