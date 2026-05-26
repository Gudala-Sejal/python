#while loop
'''a=10
while a<2:
    print(a)'''

'''a=10
while a>1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>=1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    a=a-1
    print(a)'''

'''a=20
while a>5:
    print(a)
    a+=3'''

'''a=20
while a>5:
    print(a)
    a-=1'''

'''a=9
while a<30:
    print(a)
    a+=1'''

#range()
#1.start  2.stop  3.step

'''for i in range(15):
    print(i)'''

'''for i in range(16):
    print(i)'''

'''for i in range(5,20):
    print(i)'''

'''for i in range(0,30,3):
    print(i)'''

'''for i in range (2,20,2):
    print(i)'''


'''for i in range(5,50,5):
    print(i)'''

#task
while True:
    marks=int(input("enter"))
    if marks in range(91,101):
        print("Grade-A")
    elif marks in range(81,91):
        print("Grade-B")
    elif marks in range(71,81):
        print("Grade-c")
    elif marks in range(50,71):
        print("Grade-D")
    else:
        print("Fail")



