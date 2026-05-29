# * arguments -> * is used to unpack the elements

'''a=[4,5,6,7,8,9]
print(a)
print(*a)'''

'''a=(4,5,6,7,8,9)
print(a)
print(*a)'''

'''a={4,5,6,7,8,9}
print(a)
print(*a)'''

'''a={"name":"sejal","year":2026}
print(a)
print(*a)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9,10
print(a)
print(*a)'''   #error

'''a,b,*c=2,3,4,5,6,7,8,9,10
print(a)
print(b)
print(*c)'''


'''a,*b,c=2,3,4,5,6,7,8,9,10
print(a)
print(*b)
print(c)'''

'''*a,b,c=2,3,4,5,6,7,8,9,10
print(*a)
print(b)
print(c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''   #error


'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,*b,c="codegnan"
print(a)
print(*b)
print(c)'''


#variable length arguments: These are automatically stores in tuple and we use star(*) arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(3,4,5,6,7,8,9)
b=[3,4,5,6]
check(*b)
c={8,9,10,11}
check(*c)
d={"year":2020,"name":"sejal"}
check(*d)'''

'''def check1(*a):
    d=1  #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5)
check1(2,4,5.3,2.3)
check1(1,3,4,5,2.3,4.5,"sejal",True,False,6+9j)'''

#kwargs(**)  it is a dictionary  where as * star is tuple
'''def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check2()
details={"names":["sejal","deepthi","varshitha"],"status":["p","a","p"]}
check2(**details)'''

#both ** and * usage
'''def final(*a,**b):
    d=2#creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(1,3,4,5,2.3,4.5,"sejal",True,False,6+9j)
final(*data)
details={"names":["sejal","deepthi","varshitha"],"status":["p","a","p"]}
final(**details)
final(*data,**details)'''


#task
#marks analysis report
'''no. of students  5
stu 1- 90
stu 2- 80
stu 3- 70
stu 4-60
stu 5-95

Output should be:
total students-5
highest marks-95
lowest marks=60
total marks=600
average->60.5'''


students=int(input("enter no. of students"))
total_marks=0
highest_marks=0
lowest_marks=0
average=0
for i in range(1,students+1):
    num=int(input("Enter marks: "))
    if num>i:
        print("Highest marks are: ")
    
    



