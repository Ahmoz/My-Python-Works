#Number Sorter

print("Welcome to Number Sorter!!")
print("***************************")



numbers = []

number_counter = int(input("How many numbers do you wanna sort -->>>"))

while(number_counter>0):
    x = float(input("Please enter a number"))
    numbers.append(x)
    number_counter-=1

numbers.sort()

big_or_small = int(input("If you wanna small before big press 1 big before small press 2 if you want to exit press 3-->>> "))

if(big_or_small ==1):
    for number in numbers:
        print(number)
    print("Goodbye!!")
elif big_or_small ==2:
    numbers.reverse()
    for number in numbers:
        print(number)
    print("Goodbye!!")
elif big_or_small ==3:
    print("Goodbye!!")
else:
    print("You entered an undefined number please open the program again!")