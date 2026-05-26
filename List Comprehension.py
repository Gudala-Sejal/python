'''a=["codegnan","python","course"]
b=str(a)
print(b.upper())'''

#List comprehension

'''for i in a:
    print(i.upper(),end=" ")'''

#syntax
#a=[exp for var in collection/range]


'''a=["codegnan","python","course"]
b=[i.upper() for i in a]
print(b)'''

'''a=["vja","hyd","vzg"]
b=[i.title() for i in a]
print(b)'''

'''a=[2,4,6,7,8,12,13]
b=[i**2 for i in a]
print(b)'''

'''a=[i for i in range(0,16)]
print(a)'''

'''a=[i for i in range(16) if i%2==0]
print(a)'''

'''fruits=["apple","grapes","mango","kiwi","dragon","berry"]
b=[i for i in fruits if "a" in i]
print(b)'''

#no usage of if else

#usage of else
'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[a[i]+b[i] for i in range(5)]  #a[i]+b[i] for i in range(len(a)) is another logic
print(c)

