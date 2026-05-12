Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,5.6,"python",5+9j,True,False]
print(a)
[2, 5.6, 'python', (5+9j), True, False]
typa(a)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    typa(a)
NameError: name 'typa' is not defined. Did you mean: 'type'?
type(a)
<class 'list'>
b=8.9
type(b)
<class 'float'>
c=[8.9]
type(c)
<class 'list'>

#append()
a=["python","java","c"]
a.append("ml")
a
['python', 'java', 'c', 'ml']
a.append("dsa","ai")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append("dsa","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["dsa","ai"])  #we have to pass it in square brackets to add more that is list
a
['python', 'java', 'c', 'ml', ['dsa', 'ai']]
#but it stores in square bracket again soo to avoid that we iuse method insert

#insert()
#we have to use extend not insert

#extend()
a=["ml","ai","c"]
a.extend(["python","java"])
a
['ml', 'ai', 'c', 'python', 'java']
#in avove all methods that was adding at last to get add at certain position we use insert

#insert()
a=["apple","banana","grapes"]
a.insert(1,"mango")  #1 is the index for banana we insert before banana
a
['apple', 'mango', 'banana', 'grapes']

#index()
a=["black","blue","red"."yellow"]
SyntaxError: invalid syntax
a=["black","blue","red","yellow"]
a.index("red")
2

#copy
a.copy()
['black', 'blue', 'red', 'yellow']
c=a.copy()
c
['black', 'blue', 'red', 'yellow']

#clear()
a.clear()
a
[]
b=[]
b.append("sejal")
b
['sejal']

#sort
a=["c","java","python","c++"]
a.sort()
a
['c', 'c++', 'java', 'python']
b=[3,6,9,1,0,7]
b.sort()
b
[0, 1, 3, 6, 7, 9]

#reverse
a=["python","java","c"]
a.reverse()
a
['c', 'java', 'python']
b=[4,6,9,2,8]
b.reverse()
b
[8, 2, 9, 6, 4]

#pop()
a=["hi',"helloo","byee"]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["hi","hello","byee"]
   
a.pop()
   
'byee'
#if we not mention anything it deletes last one
   
a.pop("hello")
...    
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.pop("hello")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(1)
...    
'hello'
>>> a
...    
['hi']
>>> 
>>> #remove
...    
>>> a.remove("hi"]
...    
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> a.remove("hi")
...    
>>> a
...    
[]
>>> 
>>> #length()
...    
>>> a="python"
...    
>>> len(a)
...    
6
>>> b=["python"]
...    
>>> len(b)
...    
1
>>> 
>>> #count()
...    
>>> a=["c","c++","java","python","c","c++"]
...    
>>> a.count("c")
...    
2
>>> a.count("java")
...    
1
