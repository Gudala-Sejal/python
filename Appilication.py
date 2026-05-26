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


