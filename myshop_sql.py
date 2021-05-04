print("\t\t\tWELCOME TO MY SHOP\n\t\t\t------------------")
print("1) Search\n2) Buy")
ch = int(input("Enter your Choice : "))
import mysql.connector as dd
c=dd.connect(user="root",password="62348@Mani",host="localhost",database="project",port="3306")
cur=c.cursor()
if ch == 1:
    print("1) Search by product Id : \n2) Search by Name : ")
    n = int(input("Enter your Choice : "))
    if n == 1:
        k = int(input("Enter your Product Id : "))
        cur.execute("SELECT * FROM product WHERE id=%s",(k,))
        res=cur.fetchall()
        for x in res:
            print("name : ", x[1], "\ncost : ", x[2])
    elif n == 2:
        l=input("Enter the name : ")
        l.capitalize()
        cur.execute("SELECT * FROM product WHERE ename=%s", (l,))
        res = cur.fetchall()
        for x in res:
            print("Product Id : ",x[0],"\nProduct Cost : ",x[2])
    else:
        print("Invalid input Please check again")
elif ch==2:
    k = int(input("Enter your Product Id : "))
    cur.execute("SELECT * FROM product WHERE id=%s", (k,))
    res = cur.fetchall()
    for x in res:
        print("name : ",x[1],"\ncost : ",x[2])
        q=int(input("Enter the Quantity : "))
        tot=x[2]*q
        print("Bill Amount : ",tot)
c.close()
