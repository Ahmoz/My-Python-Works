#Basic Calculator

from BasicCalculatorFuncs import Operations

print("WELCOME!!!")
print("**********")
print("What operation do you want to use??")
print("sum = 1")
print("extraction = 2")
print("product = 3")
print("division = 4")
print("exit = 5")
user_choice = int(input("your choice --->>>"))



while(user_choice != 1 and user_choice != 2 and user_choice != 3 and user_choice != 4 and user_choice != 5):
    print("You entered an undefined number! Please Try again")
    user_choice = int(input("your choice --->>>"))
    
if(user_choice==5):
    print("Goodbye!!")
    
number1 = 0
number2 = 0
if(user_choice ==1 or user_choice ==2 or user_choice ==3 or user_choice ==4):
    number1 = float(input("Choose the number 1--->>>"))
    number2 = float(input("Choose the number 2--->>>"))

op = Operations(number1,number2)


if(user_choice==1):
    result = op.summation()
elif(user_choice==2):
    result = op.extraction()
elif(user_choice==3):
    result= op.production()
elif(user_choice==4):
    result= op.division()

if(user_choice ==1 or user_choice ==2 or user_choice ==3 or user_choice ==4):
    print(f"The result is --->>> {result} ")

if(user_choice ==1 or user_choice ==2 or user_choice ==3 or user_choice ==4):
    print("Goodbye!!!")
