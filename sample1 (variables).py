Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#varibles
a=10
print(a)
10
b=20
print(b)
20
c=30
print(d)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
print(c)
30
X=40
print(x)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined. Did you mean: 'X'?
print(X)
40
z=50
print(z)
50
10=20
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
234=100
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> a123=100
>>> print(a123)
100
>>> a0123456789=100
>>> print(0123456789)
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> print(a0123456789)
100
>>> @=30
SyntaxError: invalid syntax
>>> $=90
SyntaxError: invalid syntax
>>> _=30
>>> print(_)
30
>>>  =90
...  
SyntaxError: unexpected indent
>>> _3=90
>>> print(_3)
90
>>> print=100
>>> print(print) #print is a keyword
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(print) #print is a keyword
TypeError: 'int' object is not callable
>>> name="sejal"
>>> print(name)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print(name)
TypeError: 'int' object is not callable
>>> name="sejal"
>>> print(name)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(name)
TypeError: 'int' object is not callable
>>> my_name="sejal"
>>> print(my_name)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(my_name)
TypeError: 'int' object is not callable
