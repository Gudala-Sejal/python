Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
name="sejal"
print(name)
sejal
print("name")
name
city="vja"
print("city)
      
SyntaxError: unterminated string literal (detected at line 1)
print("city")
      
city
print("vja")
      
vja
print(vja)
      
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print(vja)
NameError: name 'vja' is not defined
first name="sejal"
      
SyntaxError: invalid syntax
first_name=sejal
      
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    first_name=sejal
NameError: name 'sejal' is not defined. Did you mean: 'eval'?
first_name="sejal"
      
print(first_name)
      
sejal
fname="sejal"
      
lname="G"
      
print(fname+lname)
      
sejalG
print(fname," ",lname)
      
sejal   G
print(fname,lname)
      
sejal G
a=3,b=9
      
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=3;b=9
      
print(a+b)
      
12
a=b=c=5
      
print(a,b,c)
      
5 5 5
a,b,c=5
      
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a,b,c=5
TypeError: cannot unpack non-iterable int object
a,b,c=(4,5,6)
      
print(a,b,c)
      
4 5 6
a,b,c=3,4,5,6,7,8
      
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a,b,c=3,4,5,6,7,8
ValueError: too many values to unpack (expected 3, got 6)

a=8
      
del a
      
a
      
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> b=10
...       
>>> print(b)
...       
10
>>> delb
...       
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    delb
NameError: name 'delb' is not defined
>>> del b
...       
>>> b
...       
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> if=100
...       
SyntaxError: invalid syntax
>>> a=6
...       
>>> Age=100
...       
>>> print(Age)
...       
100
>>> age=50
...       
>>> print(age)
...       
50\
>>> AGE=
...       
SyntaxError: invalid syntax
>>> AGE=20
...       
>>> print(AGE)
...       
20
