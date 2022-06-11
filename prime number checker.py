#Prime Number Checker

num1 = int(input("What is your number --->>> "))
result = "it is prime"


for x in range(2,num1):
    if num1 % x == 0:
        result = "it is not prime"
        break


if num1 <= 1:
    result = "it is not prime"

print(result)