
#conditions
#if condition using comparison operators
#>,<,<=,>=,!=,==

#using (<)
'''a=2
b=4
if a<b:
    print("true")'''

#using (>)
'''a=10
b=20
if a>b:
    print("true")'''

#using (>=)
'''a=10
b=20
if(a>=b):
    print("yes")'''

#using (<=)
'''a=10
b=20
if (a<=b):
    print("yes")'''

#using (!=)
'''a=10
b=20
if (a!=b):
    print("yes")'''

#using (!=)
'''a=20
b=20
if (a!=b):
    print("yes")'''

#using (==)
'''a=10
b=20
if (a==b):
    print("yes")'''

#using (==)
'''a=10
b=10
if (a==b):
    print("yes")'''

#using run_tym_input of int (<)
'''a=int(input("enter a value"))
b=int(input("enter b value"))
if a<b:
    print("true")'''

#using run_tym_input of int in one variable (<)
'''a=int(input("a value"))
if a<10:
    print("true")'''

#using run_tym_operator of string (for string only uses ==, !=)
'''a="python"
if a=="python":
    print("true")'''

#using string
'''a=input("data")
if a=="ds":
    print("match")'''


#Logical operator
#using (and)
'''a=4
b=8
if a<b and b>a:
    print("true")'''

#using and (<=, >=)
'''a=4
b=8
if a<=b and b>=a:
    print("true")'''

#using and (!=, ==)
'''a=4
b=8
if a!=b and b==a:
    print("true")'''

#using or (<=.>=)
'''a=4
b=8
if a<=b or b>=a:
    print("true")'''

#using or (<,>)
'''a=4
b=8
if a<b or b>a:
    print("true")'''

#using or (!=, ==)
'''a=4
b=8
if a!=b or b==a:
    print("true")'''

#using not
'''a=4
b=8
if not a<b:
    print("true")'''

#using not (>)
'''a=4
b=8
if not a>b:
    print("true")'''

#using not and also taking logical
'''a=4
b=8
if not a<b and b>a:
    print("true")'''

#using run_tym_input
'''a=int(input("a value"))
b=int(input("b value"))
if a<b and b>a:
    print("less")'''

#using run_tym_input of string
'''a=input("data1")
b=input("data2")
if a==b:
    print("true")'''


#Identify
'''a=8
if type(a) is int:
    print("it is int")'''

#using is not
'''a=10
if type(a) is not int:
    print("true")'''

#run_tyn_input
'''a=int(input("enter"))
if type(a) is int:
    print("true")'''

#run_tym_input of float
'''a=float(input("enter value"))
if type(a) is not float:
    print("is  noot float")'''

#run_tym_input of string
'''a=input("enter")
if type(a) is str:
    print("string")'''


#Membership
'''a=[2,3,4,5,6,7,8]
if 8 in a:
    print("true")'''

#run_tym_input
'''a=int(input("enter value"))
if 10 in a:
    print("true")'''  #error

#run_tym_input
'''a=[2,3,4,5,6,7]
b=int(input("enter value"))
if b in a:
    print("present")'''

'''a=[2,3,4,5,6,7]
b=int(input("enter value"))
if b in a:
    print("present")'''


###if-else condition
#Comparison
'''a=2
b=7
if a<b:
    print("true")
else:
        print("false")'''

'''a=2
b=7
if a>b:
    print("true")
else:
    print("false")'''

#Logical
'''a=2
b=7
if a>b and b>a:
    print("true")
else:
    print("false")'''

#or
'''a=2
b=7
if a>b or b>a:
    print("true")
else:
    print("false")'''

#not
'''a=2
b=7
if not a>b and b>a:
    print("true")
else:
    print("false")'''

#Identify
'''a=2
if type(a) is int:
    print("true")
else:
    ("false")'''

#using is not
'''a=2
if type(a) is not int:
    prnt("true")
else:
    print("false")'''

#Membership
'''a=[2,3,4,5,6,7]
if 4 in a:
    print("true")
else:
    print("false")'''

#using not in
'''a=[7,8,9,10,11]
if 12 not in a:
    print("true")
else:
    print("false")'''




