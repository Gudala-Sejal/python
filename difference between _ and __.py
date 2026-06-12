#difference between single underscore(_) and double underscore(__)
class Employee():
    def __init__(self):
        self.name="pooja"
        self._mailid="pooja@codegnan.com"
        self.__salary=100000 #private variable soo we were using double underscore
class Employee1():
    def __init__(self):
            self.name="pooja"
            self._mailid="pooja@codegnan.com"
            self.__salary=90000
a=Employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._Employee__salary)
b=Employee1()
print(dir(b))
print(b.name)
print(b._mailid)
#print(b.__salary)
print(b._Employee1__salary)
