import mysql.connector as dd
c=dd.connect(user="root",host="localhost",password="62348@Mani",database="project",port="3306")
cur=c.cursor()
cur.execute("update product set ename='Pendrive' where id=2231")
c.commit()
c.close()
