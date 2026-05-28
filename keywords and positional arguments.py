#keyword and positional arguments
'''def Details(id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@codegnan.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id=10,name="sejal",mailid="s@mail.com")'''

'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid") #for heading also we can take
Details(id=10,name="sejal",mailid="s@gmail.com")
Details(id=20,name="deepthi",mailid="d@gmail.com")
Details(30,"varshitha","m@gmail.com") #without mentioning id,name,mailid
Details("lasya","l@gmail.com",40)  #giving jumbled ones
Details(mailid="a@gmail.com",name="aasya",id=50)  #giving jumbled by mentions id,name,mailid'''


#default arguments

'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("sugar",100)'''

'''def Grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("daal")'''

'''def Grocery(item="daal",price):   #default doesnot follows non default. Non-Default follows default
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(200)'''  #error


#task
'''def Bakery(item,price,qty):
    print("item is %s" %item)
    print("price is %.1f" %price)
    print("quantity is %d" %qty)
Bakery("cake",500,250)'''

'''def Bakery(item="cake",price=500,qty=250):
    print("item is %s" %item)
    print("price is %.1f" %price)
    print("quantity is %d" %qty)
Bakery()'''

'''def Bakery(item,price,qty=250):
    print("item is %s" %item)
    print("price is %.1f" %price)
    print("quantity is %d" %qty)
Bakery("cake",500)'''

'''def Bakery(item="cake",price,qty):   #error
    print("item is %s" %item)
    print("price is %.1f" %price)
    print("quantity is %d" %qty)
Bakery(500,250)'''

#task-2
'''def Split_Bill(noofpersons,amount,perhead):
    print("no. of persons is %d" %noofpersons)
    print("amount is %.2f" %amount)
    print("perhead bill is %.1f" %perhead)
Split_Bill(10,10000,1000)'''

'''def Split_Bill():
    a=int(input("enter the total no.of persons"))
    b=int(input("enter the amount"))
    print("perhead bill is",b//a)
Split_Bill()'''

'''def splitbill():   #format methid using
    a=int(input("enter the total no.of persons"))
    b=int(input("enter the amount"))
    c=b//a
    print("perhead bill is {}".format(c))
splitbill()'''

'''def splitbill():  #f"string method
    a=int(input("enter the total no.of persons"))
    b=int(input("enter the amount"))
    c=b//a
    print(f"the bill is {c}")
splitbill()'''


def splitbill():  #f"string method
    a=int(input("enter the total no.of persons"))
    b=int(input("enter the amount"))
    print("perhead bill is {}".format(b//a))
    print(f"the bill is {b//a}")
splitbill()




