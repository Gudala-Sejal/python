Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#OPERATORS
# 1.Arithematic
a=2
b=3
print(a+b)
5
print9a-b)
SyntaxError: unmatched ')'
print(a-b)
-1
print(a*b)
6
print(a//b)
0
print(a/b)
0.6666666666666666
print(a**b)
8
print(a%b)
2

#Assignment
a=4
b=2
print(a+=b)
SyntaxError: invalid syntax
a+=b
a
6
a-=3
a
3
a*=3
a
9
a//=3
a
3
a/=3
a
1.0
a%=3
a
1.0
a=2
b=8
b+=a
b
10
b-=3
b
7
b*=3
b
21
b//=3
b
7
b/=4
b
1.75
b%=3
b
1.75

#Comparison
a=5
b=9
print(a>b)
False
a<b
True
a<=b
True
a>=b
False
a!=b
True
a==b
False
b<a
False
b>a
True
b<=a
False
b>=a
True

#Logical
a=4
b=8
a<b and b>a
True
a<=d and b>=a
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a<=d and b>=a
NameError: name 'd' is not defined. Did you mean: 'id'?
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True
not true
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True

#Identify
a=10
if type(a) is int:
    print("it is int")

    
it is int
if type(a) is not int:
    print("true")

    

#Membership
    
a=1,2,3,4,5,6,7,8,9,10
if 10 in a:
    print(10)

    
10
if 20 in a:
    print(20)
... 
...     
>>> 
>>> if 20 not in a:
...     print(20)
... 
...     
20
>>> 
>>> #Bitwise
>>> a=4
>>> b=6
>>> bin(4)
'0b100'
>>> bin(6)
'0b110'
>>> a&b
4
>>> a=7
>>> b=9
>>> a|b
15
>>> a=11  #NOT operation formula is -(X+1)
>>> ~a
-12
>>> a=5
>>> b=9
>>> a^b  #XOR operator if both are 00 or 11 it becomes 0, if it is opposite 1
12
>>> a=10
>>> b=2
>>> a^b
8
>>> a=4
>>> a<<2  #Left shift in simple add zeroes to the ryt side
16
>>> a=5
>>> a<<3
40
>>> a=6
>>> a>>2  #Right shift add zeroes to the left side
1
>>> #For both left shift and right shift add zeroes and then cancel the number of digits
>>> a=3
>>> a>>4
0
