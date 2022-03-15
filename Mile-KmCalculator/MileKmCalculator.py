#Mile km calculator
import MileKmFuncs as mkf #importing mile to km and km to mile functions

#greeting
print("Welcome to Mile Km Calculator")
print("****************************")

#user decides to do what?
user_decision_check = int(input("If you want to mile to km press 1, km to mile press 2 if you want to exit press 3 -->>>> "))

#if the user enter an undefined number
while user_decision_check != 1 and user_decision_check !=2 and user_decision_check !=3:
    print("You entered undefined number! Please try again!")
    user_decision_check = int(input("If you want to mile to km press 1, km to mile press 2 if you want to exit press 3 -->>>> "))

#if the user press 3 it is invisible for him/her
if user_decision_check ==1 or user_decision_check ==2:
    theValue = float(input("What is the value do you want to change -->>>> "))


if user_decision_check ==2: #km to mile process
    user_Answer = mkf.KmToMile(theValue)
    print(f"{theValue} is now {user_Answer} in miles metric system")
    print("Thanks for choosing us!!")
elif user_decision_check ==1: #mile to km process
    user_Answer = mkf.MileToKm(theValue)
    print(f"{theValue} is now  {user_Answer} in km metric system")
    print("Thanks for choosing us!!")
elif user_decision_check == 3: #exit process
    print("Goodbye !!")
    
    
