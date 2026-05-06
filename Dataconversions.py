Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Datatypes
#int
int(6)
6
int(8.9)
8
int("sejal")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("sejal")
ValueError: invalid literal for int() with base 10: 'sejal'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

#float
float(6)
6.0
float(6.0)
6.0
float("sejal")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("sejal")
ValueError: could not convert string to float: 'sejal'
float(6+9j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(6+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0

#string
str(6)
'6'
>>> str(6.0)
'6.0'
>>> str("sejal")
'sejal'
>>> str(6+9j)
'(6+9j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> 
>>> #complex
>>> comple(1)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    comple(1)
NameError: name 'comple' is not defined. Did you mean: 'compile'?
>>> complex(1)
(1+0j)
>>> complex(4.0)
(4+0j)
>>> complex("sejal")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    complex("sejal")
ValueError: complex() arg is a malformed string
>>> complex(9+4j)
(9+4j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> #boolean
>>> bool(7)
True
>>> bool(7.0)
True
>>> bool("sejal")
True
>>> bool(6+9j)
True
>>> bool(True)
True
>>> bool(False)
False
