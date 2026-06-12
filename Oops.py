#oops
#syntax
'''class classname():
    name="sejal"
    age=20
    city="vja"
    def fname(method_name):
        print("statements..........")
obj=classname()
print(dir(a))    #it is not mandatory it's our choice
obj.fname()'''

#class declaration
'''class Details():
    name="sejal"
    age=20
    city="vja"
    def display(self):
        print(self.name,self.age,self.city)
a=Details()
print(dir(a))
a.display()'''

#object instantiation
'''class Details():
    def data(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print(self.name,self.age,self.city)

a=Details()
print(dir(a)) #here no printing of name,age,city like above ones soo check the directories
a.data("sejal",21,"vja")
a.display()
b=Details()
b.data("aargus",19,"vja")
b.display()
b.data("varshitha",21,"vja")
b.display()'''


'''class Details():
    #creating a constructor
    def __init__(self,name,age,city):    #double underscore
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print(self.name,self.age,self.city)
a=Details("sejal",21,"vja")
print(dir(a))
a.display()'''

#TASK
'''class Details():
    #creating a constructor
    def __init__(self):    #double underscore
        self.name=input("name")
        self.age=int(input("age"))
        self.city=input("city")
    def display(self):
        print(self.name,self.age,self.city)
a=Details()
print(dir(a))
a.display()'''

#another method
'''class Details():
    #creating a constructor
    def __init__(self,name,age,city):    #double underscore
        self.name=name
        self.age=age
        self.city=city
    def display(self):
        print(self.name,self.age,self.city)
a=Details(input("name"),int(input("age")),input("city"))
print(dir(a))
a.display()'''
    

