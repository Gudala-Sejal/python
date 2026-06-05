#Regex- Regular expressions or powerful tools (module) embedded in python which is mainly used to find a pattern within a given string or statements or files and we mainly used for text manipulation.

'''a="codegnan is in vja"
print(a)'''

'''a="codegnan\nis\tin\nvja"
print(a)'''

#rstring(raw string)- doesnot change anything
'''a=r"codegnan\nis\tin\nvja"
print(a)'''

#compile(),search(),findall(),split(),sub()->substitute
#sequence characters
'''\w->it matches alphanumeric
\W->it matches non-alphanumeric
\d->it matches any digit
\D->it matches non-digit
\s->it represents white spaces
\S->it represents non-white spaces'''

#compile()->it doesnot do anything
'''import re
a="main mat map cat money cash maths cup code monkey dog donkey"
b=re.compile(r"m\w")
print(b)'''

#search->
'''import re
a="main mat map cat money cash maths cup code monkey dog donkey"
b=re.compile(r"m\w\w\w")  #\w-2 letters next one and so onn -> to know the difference we were using search
print(b)
c=b.search(a)
print(c)'''

'''d=re.search(r"m\w+",a)
print(d)'''

#find all()
'''d=re.findall(r"m\w+",a)
print(d)
print(*d) #to unpack'''

#split
'''import re
a="main mat map cat money cash maths cup code monkey dog donkey"'''
'''e=re.split(r"m",a)
print(e)'''

'''f=re.split(r"\s",a)
print(f)'''

#sub()
'''x=re.sub(r"m","k",a)
print(x)

x=re.sub(r"maths","science",a)
print(x)'''

#task->using \d
'''import re
a="map 9 mat dog donkey 3 4 cup 2 maths code money 5 7"
b=re.findall(r"\d",a)
print(*b)'''

'''a="year 2026 month 6 date 05"
b=re.findall(r"\d",a)
print(b)

b=re.findall(r"\d+",a)
print(b)'''


