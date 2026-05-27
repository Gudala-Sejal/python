'''while True:
    weight=int(input("enter weight"))
    height=float(input("enter height"))
    bmi=weight/height**2
    if bmi==18.5:
            print("Healthy weight")
    elif bmi>18.5 and bmi<24.5:
        print("Normal weight") 
    elif bmi>24.5 and bmi<=29.5:
        print("Overweight")
    elif bmi>=30:
        print("Obesity")'''

#Railway ticket
'''while True:
    ticket=1000
    gender=input("enter gender")
    age=int(input("enter age"))
    if gender=="m":
        if age>=60:
            print("senoir citizen")
            ticket=ticket-30/100*ticket
            print(ticket)
        elif age<60:
            print("normal citizen")
            print(ticket)
    elif gender=="f":
        if age>=60:
            print("senior citizen")
            ticket=ticket-30/100*ticket
            print(ticket)
        elif age<=60:
            print("normal citizen")
            print(ticket)'''


#attendance report
'''students=int(input("enter no. of students"))
p=0
a=0
for i in range(1,students+1):
    c=input(f"enter the student attendace {i}")
    if c=="p":
        p+=1
    elif c=="a":
        a+=1
print("Attendence Report......................")
print("Total Students",students)
print("Total Presentiess",p)
print("Total Absentiess",a)'''



#Patterns
'''1.right angle
*
* *
* * *
* * * *
* * * * *

2.revese right angle
* * * * *
* * * *
* * *
* *
*

3.square
* * * *
* * * *
* * * *
* * * *

4.pyramid
   *
  * *
 * * *
* * * *'''

#1.right angle
'''rows=5                   
for i in range(1,rows+1):
    print("*" * i)'''
    

#2.reverse right angle
'''rows=5                     '''n=int(input("enter no of rows"))
for i in range(rows,0,-1):       for i in range(n):
    print("*" * i)'''              print("*"*(n-i))'''

'''#3.square
rows=4
cols=4           #we can take as run tym input asn=int(input()) 
for i in range(rows):
    for j in range(cols):
        print("*",end=" ")
    print()'''

#pyramid
'''rows=1
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    print()'''
