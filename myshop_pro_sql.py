print("\t\t\tWELCOME TO MY SHOP\n\t\t\t------------------")
print("1) Search\n2) Buy")
class myshop:
    def values(self):
        ch = int(input("Enter your Choice : "))
        import mysql.connector as dd
        c = dd.connect(user="root", password="62348@Mani", host="localhost", database="project", port="3306")
        cur = c.cursor()
        if ch == 1:
            print("1) Search by product Id : \n2) Search by Name : ")
            n = int(input("Enter your Choice : "))
            if n == 1:
                k = int(input("Enter your Product Id : "))
                cur.execute("SELECT * FROM product WHERE id=%s", (k,))
                res = cur.fetchall()
                for x in res:
                    print("name : ", x[1], "\ncost : ", x[2])
                    self.f = x[2]
                    myshop.buy(self)
            elif n == 2:
                l = input("Enter the name : ")
                l.capitalize()
                cur.execute("SELECT * FROM product WHERE ename=%s", (l,))
                amt = cur.fetchall()
                for m in amt:
                    print("Product Id : ", m[0], "\nProduct Cost : ", m[2])
                    self.f=m[2]
                    myshop.buy(self)
            else:
                print("Invalid input Please check again")
        elif ch == 2:
            k = int(input("Enter your Product Id : "))
            cur.execute("SELECT * FROM product WHERE id=%s", (k,))
            zan = cur.fetchall()
            for z in zan:
                print("name : ", z[1], "\ncost : ",z[2])
                self.f = z[2]
                myshop.amount(self)
    def amount(self):
        q = int(input("Enter quantity : "))
        tot = q * self.f
        print("bill amount : ",tot)
    def buy(self):
        by=input("Do you want to buy (y/n) : ")
        if by=="y" or by=="Y":
            myshop.amount(self)
class product(myshop):
    def process(self):
        myshop.values(self)

cal=product()
cal.process()