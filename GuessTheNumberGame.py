import random

print("Welcome to the number guessing game")
print("****************************")

user_live= int(input("How many lives do you want?--->>"))

startnum=int(input("start from?? -->>>"))
stopnum = int(input("stop where?? -->>>"))


number1 = random.randint(startnum,stopnum)


while(user_live!=0):
    number2= int(input("guess the number"))
    if number2==number1:
        print("YEEES IT IS CORRECT")
        break
    user_live-=1
    

if(user_live==0):
    print("You couldn`t know sorry :(")