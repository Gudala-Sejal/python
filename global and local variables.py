#global and local variables
#first case of global variable
'''a=2
def check1():
    print("a value is : ",a)
check1()
print("a value is: ",a)'''

#second case
'''a=3
def check2():
    a=5
    a=a**2
    print("inside value is",a)
check2()
print("the value of a is",a)'''

#third case of global variable and local variables
'''a=4
def check3():
    a=6
    print("the value of a is: ",a)
    a=5
    print("the value of a is: ",a+4)
    b=12 #local varible
    b=b+a
    print("the value of b is: ",b)
check3()
print("the value of a is: ",a)
print("the value of b is: ",b)'''

#usage of global keyword
'''a=4
def final():
    global a
    print("inside value of a",a)
    a=15
    print("updated value of a",a)
    b=20
    b=b+a
    print("b value is",b)
final()
print("the value of a",a)
print("the value of b is",b)''' #it is error becoz we not mention global b

'''a=4
def final():
    global a,b
    print("inside value of a",a)
    a=15
    print("updated value of a",a)
    #global b
    b=20
    b=b+a
    print("b value is",b)
final()
print("the value of a",a)
print("the value of b is",b)'''



