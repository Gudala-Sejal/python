#Error handling
''' They are three types
1.Syntax error-> Compile Error
2.Run time Error-> During execution time
3.Logical Error-> Error in logic(it can't visible)'''

#Syntax error
'''for i in range(10):
    print(i)'''

'''for i in range(10)
  print(i)'''

'''for i in range(10):
print(i)'''

#Run time error
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)''' #->during execution like giving string in place string or not divisible

#Logical Error
'''a=10
b=20
if a<b:
    print("true")'''

'''a=10
b=20
if a>b:
    print("true")'''


#Exception Handling
'''1.Try->instructions from which we are expecting the exceptions
2.except-> exception is raised in try block it will be handle by this block
3.else-> optional(no exception)
4.finally-> always'''

'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
   try:      
        c=a//b
        print(c)'''

while True:
        a=int(input("a value"))
        b=int(input("b value"))
       try:
           c=a//b
           print(c)
        except:   
            print("exception is raised")
        else:   #it enters only when try block is true
            print("no exceptional")
        finally:   #it always execute whether it is true or not
            print("the program ends here")
     
