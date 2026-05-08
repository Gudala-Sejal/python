Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing
a="vijayawada"
a[7]
'a'
a[0]+a[1]+a[2]
'vij'
a="vijayawada is a royal city"
a[22]+a[23]+a[24]+a[25]
'city'
a[11]+a[12]+a[13]+a[14]
'is a'
   #Negative indexing
a="codegnan it solutions"
a[-9]+a[-8]+a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'solutions'

#Slicing
a="codegnan"
a[0]+a[1]+a[2]+a[3]
'code'
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a="wait until you succeed"
a[15:22]
'succeed'
a[11:14]
'you'
a[5:10]
'until'
a[0:4]
'wait'
b="simple is better than complex"
a[22:29]
''
a[10:16]
' you s'
b[22:29]
'complex'
b[10:16]
'better'
b[0:6]
'simple'
a[:6]
'wait u'
b[:6]
'simple'
b[17:21]
'than'
a="kill them with your success"
a[-17:-13]
'with'
a[-12:-9]
'you'
a[-27:-23]
'kill'
a[-7:0]
''
a[-7:-1]
'succes'
a[-7:]
'success'
b="all is well"
b[-7:-5]
'is'
b[-11:-8]
'all'
b[-4:]
'well'

#Striding
#syntax is [a:b:c]  here a is starting, b is ending then c is increment
a="data science"
a[::]
'data science'
a[::1]
'data science'
#here the starting is d then increment is 1 soo add 0+1 then 1 it is a, then for 1 add1 it is 2 that a and so on....
a[::2]
'dt cec'
a="cloud computing"
a[::3]
'cucpi'
a[::5]
'c u'
>>> a[::7]
'cog'
>>> a[::4]
'cdmi'
>>> #Slicing question
>>> a[1:6]
'loud '
>>> a[5:]
' computing'
>>> a[:9]
'cloud com'
>>> a[7:12]
'omput'
>>> a="machine learning"
>>> a[1:7:2]
'ahn'
>>> #here first thake 1:7 that goes on slicing then increment
>>> a[2:14:3]
'cnlr'
>>> a[3:15:5]
'hli'
>>> a[5:12:2]
'n er'
>>> a="python course"
>>> a[-1:-8:-3]
'eu '
>>> a[-2:-12:-4]
'sch'
>>> a[-3:-13:-5]
'rn'
>>> a[-5:-11:-2]
'o o'
>>> #Do's and Dont's of Strinding
>>> #in book
>>> #example is
>>> a[9:4:2]
''
>>> #none because for positive striding highest to loweas not possible
>>> a[-6:-3:-1]
''
>>> #for negative striding lowest to highest is not possible
>>> a[::-1]
'esruoc nohtyp'
>>> a[::1]
'python course'
