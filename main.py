import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "cars"
)

def creg():
    cmodel = input("Enter car name: ")
    price = input("Enter car price:")
    qty = input("Total cars:")
    ccode = input("Enter car code:")
    data = (cmodel,price,qty,ccode)
    sql = "insert into creg(cmodel,price,qty,ccode) values(%s,%s,%s,%s)"
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print(".............")
    print("Data entered successfully")
    main()


def csell():
    owner = input("Enter owner:")
    ccode = input("Enter car code:")
    date = input("Enter date:")
    price = input("Enter the price:")
    sql  = "insert into csell(owner, ccode, date, price) values(%s,%s,%s,%s)"
    data =(owner, ccode, date, price)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    print("...............")
    print("car issued to :",owner)
    main()



def cdel():
    ccode = input("Enter car code:")
    sql = "delete from creg where ccode = %s"
    data = (ccode,)
    c = mydb.cursor()
    c.execute(sql,data)
    mydb.commit()
    main()


def discars():
    sql = "select * from creg"
    c = mydb.cursor()
    c.execute(sql)
    myresult = c.fetchall()
    for i in myresult:
        print("cmodel:",i[0])
        print("qty:",i[1])
        print("price:",i[2])
        print("ccode:",i[3])
        print("................")
    main()


def main():
    print("""............CARS.............
    1.Add car
    2.sell car
    3.delete car
    4.Display car
    """)
    choice = input("Enter task no:")
    print("............................")
    if(choice == '1'):
        creg()
    elif(choice == '2'):
        csell()
    elif(choice == '3'):
        cdel()
    elif(choice == '4'):
        discars()
    else:
        print("wrong choice")
main()
