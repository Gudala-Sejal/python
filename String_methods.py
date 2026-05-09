Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""l
SyntaxError: invalid syntax
c=""
len(c)
0
d=" "
len(d)
1

#count()
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("k")
2
a.count(" ")
3

#escape sequences
#\n->new line
#\t->tab space
a="name\nmobileno\tmailid"
print(a)
name
mobileno	mailid
b="name:Sejal\nmobileno:8096989899\tmailid:sejalsrinivas2005@gmail.com"
print(b)
name:Sejal
mobileno:8096989899	mailid:sejalsrinivas2005@gmail.com

#replace()
a"wait until you succeed"
SyntaxError: invalid syntax
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a="code"
a[0]
'c'
a.find("d")
2
#above is find a string
#upper()
a="python"
a.upper()
'PYTHON'
#lower()
a="PYTHON"
a.lower()
'python'
c="python"
c.capitalize()
'Python'
d="pyhton course"
d.title()
'Pyhton Course'
e="i am in class"
e.title()
'I Am In Class'
e.captilize()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    e.captilize()
AttributeError: 'str' object has no attribute 'captilize'. Did you mean: 'capitalize'?
e.capitalize()
'I am in class'
a="hello"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="hello world"
b.isalpha()
False
c="helloworld"
c.isalpha()
True
d=890
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
e="12345"
e.isdigit()
True
x="sejal1234"
x.isalnum()
True
y="sejal@1234"
x.isalnum()
True
y.isalnum()
False

#strip
#lstrip()
#rstrip()
a="        sejal       "
a.strip()
'sejal'
a.lstrip()
'sejal       '
a.rstrip()
'        sejal'

#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am learning python"
b.split()
['i', 'am', 'learning', 'python']

#join()
a="python","c","c++"
"".join(a)
'pythoncc++'
" ".join(a)
'python c c++'

#concatenation
a="python"
b="course"
print(a+b)
pythoncourse
>>> print(a+" "+b)
python course
>>> fname="sejal"
>>> lname="g"
>>> print(fname+lname)
sejalg
>>> print(fname+" "+lname)
sejal g
>>> print(fname.title()+" "+lname.title())
Sejal G
>>> print((fname+" "+lname).title())
Sejal G
>>> 
>>> #formatting
>>> a=3
>>> b=7
>>> print(a+b)
10
>>> print("the sum is",a+b)
the sum is 10
>>> print("the sum is,a+b")
the sum is,a+b
>>> city="vja"
>>> print("city is",city)
city is vja
>>> 
>>> #format method
>>> a="motu"
>>> b="patlu"
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> print("hello {} {}".format(a,b))
hello motu patlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello patlu
>>> 
>>> #fstring
>>> a="chota"
>>> b="bheem"
>>> print(f"hello {a}{b}")
hello chotabheem
>>> print(f"hello {a} {b}")
hello chota bheem
>>> print(f"hello {a} hello {b}")
hello chota hello bheem
