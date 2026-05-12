Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
  ##TUPLE
a=(5,6.7,"sejal",4+9j,True,False)
print(a)
(5, 6.7, 'sejal', (4+9j), True, False)
type(a)
<class 'tuple'>

#length()
len(a)
6

#count()
a.count(True)
1

#index
a.index(4+9j)
3
   ##SETS
#mention in{} flower barckets
a={3,6.7,"sejal",4+9j,True,False}
print(a)
{False, True, 3, 6.7, 'sejal', (4+9j)}
type(a)
<class 'set'>
b={4,5,6,9,3}
type(b)
<class 'set'>

#issubset
a={1,2,3,4,5,6,7,8,9}
b={4,5,8,9}
b.issubset(a)
True
b.issubset(b)
True
a.bsubset(b)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.bsubset(b)
AttributeError: 'set' object has no attribute 'bsubset'. Did you mean: 'issubset'?
a.issubset(b)
False

#superset()
a={4,5,6,7,8,9}
b={7,8,9}
a.issuperset(b)
True

#union
a={3,4,5,6,7}
b=(1,2,3,4,5,6,7,8,9}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
b={1,2,3,4,5,6,7,8,9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#intersection
a={2,3,4,5,6,7}
b={5,6,7}
a.intersection(b)
{5, 6, 7}

#update()
a={10,11,12,13,14,15}
b={13,14,15,16,17}
a
{10, 11, 12, 13, 14, 15}
a.update(b)
a
{10, 11, 12, 13, 14, 15, 16, 17}
b
{16, 17, 13, 14, 15}
b.update(a)
b
{10, 11, 12, 13, 14, 15, 16, 17}

#difference
a={2,3,4,5,6,7,8}
b={7,8,9,10,11,12}
a.difference(b)
{2, 3, 4, 5, 6}
b.difference(a)
{9, 10, 11, 12}
b
{7, 8, 9, 10, 11, 12}

#symmetric_difference()
a={2,3,4,5,6,7,8}
b={1,5,6,7,8,9,10}
a.symmetric_difference(b)
{1, 2, 3, 4, 9, 10}
b.symmetric_difference(b)
set()
b.symmetric_difference(a)
{1, 2, 3, 4, 9, 10}

#difference_update()
a={2,3,4,5,6,7,8}
b={7,8,9,10,11,12}
a.difference_update(b)
a
{2, 3, 4, 5, 6}
b.difference_update(a)
b
{7, 8, 9, 10, 11, 12}

#symmetric_difference_update()
a={2,3,4,5,6,7,8}
b={1,5,6,7,8,9,10}
a.symmetric_difference_update(b)
a
{1, 2, 3, 4, 9, 10}
b.symmetric_difference_update(a)
b
{2, 3, 4, 5, 6, 7, 8}

#intersection_update()
a={10,20,30,40,50,60}
b={40,50,60,70,80}
a.intersection_update(b)
a
{40, 50, 60}
b.intersection_update(a)
b
{40, 50, 60}

#pop
a={6,7,8,9,10,11,12,13}
a.pop()
6
a.pop(9)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    a.pop(9)
TypeError: set.pop() takes no arguments (1 given)

#remove
a.remove(9)
a.remove(11)
a
{7, 8, 10, 12, 13}

#discard()
a={5,6,7,8,9}
a.discard(8)
a
{5, 6, 7, 9}

#index
>>> a.index(2)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'
>>> 
>>> #count()
>>> a.count(6)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    a.count(6)
AttributeError: 'set' object has no attribute 'count'
>>> 
>>> #disjoint
>>> a={4,5,6,7,8}
>>> b={6,7,8,9,10,11}
>>> a.isdisjoint(b)
False
>>> a={3,4,5,6,7}
>>> b={8,9,10,11,12}
>>> a.isdisjoint(b)
True
>>> 
>>> #clear()
>>> a={5,6,7,8,9}
>>> a.clear()
>>> a
set()
>>> 
>>> #add
>>> b=set()
>>> b.add(10,11)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    b.add(10,11)
TypeError: set.add() takes exactly one argument (2 given)
>>> b.add(10)
>>> b
{10}
>>> 
>>> #copy
>>> a={6,7}
>>> a.copy()
{6, 7}
>>> a
{6, 7}
