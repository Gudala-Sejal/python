'''a=10
b=20
print("The sum is: ",a+b)
print("The difference is: ",a-b)
print("The product is: ",a*b)
a=100
b=200
print("The sum is: ",a+b)
print("The difference is: ",a-b)
print("The product is: ",a*b)
a=1000
b=2000
print("The sum is: ",a+b)
print("The difference is: ",a-b)
print("The product is: ",a*b)'''


#in above code the lines of code was incresing to reduce that we use FUNCTIONS
#FUNCTIONS
'''def calculate(a,b):
    print("The sum is: ",a+b)
    print("The difference is: ",a-b)
    print("The product is: ",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''


'''def calculate(a,b):
    print("The integer division value is: ",a//b)
    print("The modulo division is: ",a%b)
    print("The power is: ",a**b)
calculate(2,3)
calculate(3,4)
calculate(4,5)'''

'''def add(a,b):
    print(a+b)
add(4,5)'''

'''def add():
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    print(a+b)
add()'''

'''def fullname():
    a=input("First name:")
    b=input("Last name:")
    print((a+" " +b).title())
fullname()'''


'''while True:
    def calculate():
        a=int(input("Enter a"))
        b=int(input("Enter b"))
        options=int(input("Choose option 1.add 2.difference 3.product"))
        if options==1:
            print(a+b)
        if options==2:
            print(a-b)
        if options==3:
            print(a*b)
    calculate()'''


#task
#using multiple def
'''def add():
    print(a+b)
def sub():
    print(a-b)
def pro():
    print(a*b)
while True:
    a=int(input("Enter a value"))
    b=int(input("Enter b value"))
    option=int(input("Choose the option
                     1.add
                     2.sub
                     3.pro"))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        pro()'''


#print vs return
'''def add(a,b):
    print(a+b)
add(2,4)'''

'''def add(a,b):
    return a+b
print(add(2,4))'''


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(4,6)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(4,2))'''
