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
'''class New():
    def sum(self,a=3,b=4,c=5):
        if a!=3 and b!=4 and c!=5:
            print("The sum is ",a+b+c)
        elif a==3 and b==4:
            print("The product is ",a*b)
        else:
            print("The program ends")
a=New()
a.sum()'''


#Method overriding
'''class Animal():
    def speak(self):
        print("Animals make the sounds")
class Dog():
    def speak(self):
        print("Dog can barks")
c=Animal()
d=Dog()
c.speak()
d.speak()'''

#single Inheritance- From single parent to single child
'''class RBI():  #parent
    cash=100000
    def available_cash(cls):
        print("avaliable cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(): #child-1
    pass
class HDFC(RBI): #child-2
    cash=50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a=HDFC()
a.available_cash()
a.new_cash()'''

#Multiple Inheritance- Two paremts and one child
'''class Father():
    def weight(cls):
        print("The weight is 50kgs")
class Mother():
    def height(cls):
        print("The height is 5ft")
class Child(Father,Mother):
    def DOB(cls):
        print("Justt Born.....")
a=Child()
a.weight()
a.height()
a.DOB()'''

#Multilevel
'''class GrandParent():
    def land(self):
        print("The land")
class Parent(GrandParent):
    def house(self):
        print("The house")
class Child(Parent):
    def vehicle(self):
        print("The vehicle")
a=Child()
a.land()
a.house()
a.vehicle()'''
        

#Hierarchial Inheritance- it is a company where parent class is inherited by multiple child classes
#Hybrid- It means combining one or more than one type of inheritance for example hierarchial + multiple inheritance

#Hierarchial
'''class Employee:
    def company(self): #parent class
        print("codegnan it solutions")
class Trainer(Employee):
    def Teach(self):  #child-1
        print("teaches the code")
class Devloper(Employee):
    def devlop(self):  #child-2
        print("devlopes the code")
a=Trainer()
a.Teach()
a.company()
b=Devloper()
b.devlop()
b.company()'''

#Hybrid
'''class Person:
    def details(self):
        print("details of person")
class Teacher(Person):
    def teach(self):
        print("teach the code")
class Student(Person):
    def study(self):
        print("studies the code")
class Teaching_Assistant(Teacher,Student):
    def work(self):
        print("python")
a=Teaching_Assistant()
a.details()
a.teach()
a.study()
a.work()'''

#super- builtin function
'''class parent():
    def __init__(self,name):
        self.name=name
        print("parent constructor")
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
        print("child constructor")
a=child("sejal",21)
print(a.name)
print(a.age)'''


#PROJECT-Written in notes

#Encapsulation
#publicdata
'''class Parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class Child(Parent):
    def method2(self):
        print(self.publicdata)
obj1=Parent()
obj2=Child()
obj1.method1()
obj2.method2()'''

#_protecteddata
'''class Parent():
    _protecteddata=100
    def method1(self):
        print(self._protecteddata)
class Child(Parent):
    def method2(self):
        print(self._protecteddata)
obj1=Parent()
obj2=Child()
obj1.method1()
obj2.method2()
print(obj1._protecteddata)
print(obj2._protecteddata)'''

#__privatedata
'''class Parent():
    __privatedata=100
    def method1(self):
        print(self.__privatedata)
class Child(Parent):
    def method2(self):
        print(self._Parent__privatedata)  #we have to take single underscore with parenth then double underscore so it doesnot shows error
obj1=Parent()
obj2=Child()
obj1.method1()
obj2.method2()'''


#Abstraction
'''class A():
    def method1(self):
        pass
obj1=A()
obj1.method1()'''

'''class A():
    def method1(self):
        print("data")
obj1=A()
obj1.method1()'''

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        print("python")
obj1=A()
obj1.method1()'''   #here it is error because we taking only one method

'''from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def method1(self):
        pass
    def method2(self):
        print("method2 is implemented")
    def method3(self):
        pass
class B(A):
    def method1(self):
        print("method1 is implemented")
    def method3(self):
        print("method3 is implemented")
obj1=B()
obj1.method1()
obj1.method3()
obj1.method2()'''          #here implemented bcoz we were taking more than one method





