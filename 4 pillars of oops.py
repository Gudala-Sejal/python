#polymorphism
#1.operator overloading - Using one operators at multiple variations
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(8))
print(a.__sub__(1))
print(a.__mul__(2))
print(a.__pow__(2))
#print(a.__div__(2))
print(a.__ge__(6))  #greater than or equal to
print(a.__le__(8))
print(a.__eq__(4))
a=[2,3,4,5,6];b=[7,8,9,10,11]
print(a+b)
print(a.__add__(b))
print(a.__getitem__(3))  #index
print(b.__getitem__(2))
a="code";b="gnan"
print(a+b)
print(a.__add__(b))
a="python";b="course"
print(a.__add__(" "+b))  #" " used for space
print("pooja".__add__(" "+"ch").title())'''


#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(3)
y=B(4)  #if we mention classes then output will be the 3*4 that has given in class A
#x=3  If we don't mention classes then output will be 3+4
#y=4
print(x+y)'''

#method overloading- Using a method number of times
'''class New():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("The product is",a*b)
        else:
            print("program Ends")
a=New()
a.sum()
a.sum(2,3,4)
a.sum(5,6)'''

#TASK
class New():
    def sum(self,a=3,b=4,c=5):
        if a!=3 and b!=4 and c!=5:
            print("The sum is ",a+b+c)
        elif a==3 and b==4:
            print("The product is ",a*b)
        else:
            print("The program ends")
a=New()
a.sum()
                  
                
