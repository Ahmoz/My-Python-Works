import random
originalnumber = random.randint(0,100)

guessnumber = -1
while int(guessnumber) != originalnumber:
    guessnumber = input("Guess the number: ")
    if int(guessnumber) < originalnumber:
        print("Try a little big")
    elif int(guessnumber) > originalnumber:
        print("Try a little small")
    
if int(guessnumber) == originalnumber:
    print("Correct answer congratulations :) ")