Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
  ##dictionary
a={"name":"pooja","year":2026,"month":5}
print(a)
{'name': 'pooja', 'year': 2026, 'month': 5}
type(a)
<class 'dict'>
b={"name","sejal","year",2026}
print(b)
{'sejal', 'year', 2026, 'name'}
type(b)
<class 'set'>
#accessing data
a["name"]
'pooja'
a[2026]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[2026]
KeyError: 2026

#keys()
a.keys()
dict_keys(['name', 'year', 'month'])

#values()
a.values()
dict_values(['pooja', 2026, 5])

#items()
a.items()
dict_items([('name', 'pooja'), ('year', 2026), ('month', 5)])

#update()
a={"year":2026,"month":"may"}
a.update({"date":12})
a
{'year': 2026, 'month': 'may', 'date': 12}
a.update({"date":12},{"time":7})
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.update({"date":12},{"time":7})
TypeError: update expected at most 1 argument, got 2
a.update({"date":12,"time":7})
a
{'year': 2026, 'month': 'may', 'date': 12, 'time': 7}
a={"mobileno":8096989899,"mail id":sejal@gmail.com}
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    a={"mobileno":8096989899,"mail id":sejal@gmail.com}
NameError: name 'sejal' is not defined. Did you mean: 'eval'?
a={"mobileno":8096989899,"mail id":s@gmail.com}
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a={"mobileno":8096989899,"mail id":s@gmail.com}
NameError: name 's' is not defined
a={"mobileno":8096989899,"mail id":"sejal@gmail.com"}
a.setdefault("name":"sejal")
SyntaxError: invalid syntax
a.setdefault("name","sejal")
'sejal'
a
{'mobileno': 8096989899, 'mail id': 'sejal@gmail.com', 'name': 'sejal'}

#get()
a={"color":"black","food":"biryani"}
a.get("color")
'black'

#copy()
a.copy()
{'color': 'black', 'food': 'biryani'}

#pop
a.pop()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("color")
'black'
a
{'food': 'biryani'}

>>> a.pop(0)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.pop(0)
KeyError: 0
>>> 
>>> #popitem()
>>> a.popitem()
('food', 'biryani')
>>> b={"mobileno":8096989899,"mail id":sejal@gmail.com}
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    b={"mobileno":8096989899,"mail id":sejal@gmail.com}
NameError: name 'sejal' is not defined. Did you mean: 'eval'?
>>> b={"mobileno":8096989899,"mail id":"sejal@gmail.com"}
>>> b.popitem()
('mail id', 'sejal@gmail.com')
>>> b
{'mobileno': 8096989899}
>>> 
>>> #clear()
>>> b.clear()
>>> b
{}
>>> 
>>> #duplicates
>>> a={"name":"sejal","year":2026,"name":"sejal"}
>>> print(a)
{'name': 'sejal', 'year': 2026}
>>> a={"name":"sejal","year":2026,"name":"sejal gudala"}
>>> print(a)
{'name': 'sejal gudala', 'year': 2026}
>>> a={"name":"sejal","year":2026,"name1":"sejal"}
>>> print(a)
{'name': 'sejal', 'year': 2026, 'name1': 'sejal'}
>>> 
>>> #single key number of values
>>> a={"idnos":[10,20,30],"names":["sejal","deepthi","varshitha"],"marks":[60,70,80]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['sejal', 'deepthi', 'varshitha'], 'marks': [60, 70, 80]}
>>> a.keys()
dict_keys(['idnos', 'names', 'marks'])
>>> a.values()
dict_values([[10, 20, 30], ['sejal', 'deepthi', 'varshitha'], [60, 70, 80]])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['sejal', 'deepthi', 'varshitha']), ('marks', [60, 70, 80])])
