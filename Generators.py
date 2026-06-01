#GENERATORS
'''a=[i for i in range(16)]
print(a)
print(type(a))'''

'''a=(i for i in range(16))
print(*a)   #we have to mention * to get the output
print(type(a))''' 

'''a=(i for i in range(16))
#print(list(a))
#print(tuple(a))
#print(set(a))
print(set(*a))'''  #we cannot pass at a time

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))''' 

'''a,b=[int(x) for x in input("enter the values").split(",")]
def check(a,b):
    while a<b:
        a=a+1
    return a
print(check(a,b))''' #here it print last iteration only bcoz we mention return a at the outside of while loop

#yield Vs return
'''def  mygen():
    return "python"
    return "dsa"
    return "java"
print(mygen())'''

'''def  mygen():
    #return "python"
    #return "dsa"
    #return "java"
    return "python","dsa","java"
print(mygen())'''

'''def  mygen():
    yield "python"
    yield "dsa"
    yield "java"
print(*mygen())

#next
d=mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))'''

#max()
'''print(max(3,4,5,67,7,8,21))'''

#min()
'''print(min(2,3,402,20,49))'''

#sum
#print(sum(2,3)) error
a=2,3,4,5,6,7
'''print(sum(a))'''






