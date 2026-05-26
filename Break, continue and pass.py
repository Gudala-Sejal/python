'''#break
a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a)'''

'''for i in range(21):
    if i==14:
        break
    print(i)'''

'''a="python"
for i in a:
    print(i)'''

'''a="python"
if a=="h":
    break
print(a) #error'''

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''


#continue
'''a=20
while a>5:
    print(a)
    a=a-1'''

'''a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        continue #doesnot skip 10 bcoz we were giving print before'''

'''a=20
while a>4:
    a=a-1
    if a==10:
        continue
    print(a)'''

'''for i in range(15):
    if i==9:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="h":
        continue
    print(i)'''

#pass
'''a=25
while a>1:
    print(a)
    a=a-1
    if a==15:
        pass'''

'''for i in range(15):
    if i==10:
        pass
    print(i)'''



#ATM Appilication
'''Account_balance=100000
card=input("enter card")
if card=="c":
    print("Welcome Sejal")
password=int(input("enter password"))
if password==1234:
    print("Correct")
    options=int(input("choose the option 1.Balance 2.withdraw"))
    if options==1:
        print("The account balance is 100000")
    elif options==2:
        cash=int(input("withdrawn amount"))
        print("The balance is",100000-cash)
    else:
        print("Invalid option")
else:
    print("incorrect password")'''


while True:
    account=100000
    pwd=1234
    card=input("insert the card")
    if card=="c":
        print("welcome sejal")
        password=int(input("enter password"))
        if password==pwd:
            option=int(input('''choose the option 1.balance enquiry  2.Withdrawl'''))
            if option==1:
                print("your account balance is",account)
            elif option==2:
                money=int(input("enter the amount"))
                print(money)
                balance=account-money
                print("the reamining is: ",balance)
            else:
                print("invalid option")
        else:
            print("invalid password")
    else:
        print("invalid card")
                


               

