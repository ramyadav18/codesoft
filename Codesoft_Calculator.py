a = int(input("Enter a 1st Number : "))
b = int(input("Enter a 2st Number : "))

print ('''
       what You want !!      
          1 = Addition
          2 = Subtraction
          3 = Multiplication
          4 = Divide
          5 = Modulo
''')
select = int(input("Please enter your choice from 1 to 5 : "))

if select == 1:
    print (f"Addition of {a} and {b} is : ",a+b)
elif select == 2:
    print (f"Subtraction of {a} and {b} is : ",a-b)
elif select == 3:
    print (f"Multiplication of {a} and {b} is : ",a*b)
elif select == 4:
    print (f"Divide of {a} and {b} is : ",a/b)
elif select == 5:
    print (f"Modulo of {a} and {b} is : ",a%b)
else: 
    print ("Please select a Valid Choice ")


        