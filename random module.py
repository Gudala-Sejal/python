#random module

#sample
'''import random
a=random.sample(range(20,40),5)
print(a)'''

#randint()
'''import random
a=random.randint(30,50)
print(a)'''

#choice
'''import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)'''

#task dice
'''import random
while True:
    n=int(input("Enter the roll of dice"))
    a=random.randint(1,6)
    print(a)
    option=int(input("choose the option
                                         1.yes
                                         2.no"))

    if option==1:
         continue
    elif option==2:
         break'''

                                         
#calendar module
'''import calendar
year=2026
month=6
print(calendar.month(year,month))'''

'''import calendar
year=2027
print(calendar.calendar(year))'''

'''import calendar
year=int(input("Enter a year"))
month=int(input("Enter a month"))
print(calendar.month(year,month))'''

#date & time
'''from datetime import date
a=date.today()
print(a)'''

'''import datetime
a=datetime.datetime.now()
print(a)'''

#epoch time
'''import time
a=time.time()
print(a)

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"now the time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"the day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")'''

#task
'''import random
import time
for i in range(10):
    a=random.randint(1000,9999)
    print(a)
    time.sleep(2)'''



