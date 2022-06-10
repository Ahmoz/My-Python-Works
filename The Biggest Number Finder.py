#finder the biggest number

#greeting
print("Welcome")
print("************")

#creating the list
list_of_the_nums = []

#how many nums
how_many_nums = int(input("How many numbers do you wanna compare--->>> "))

#creating the counter
counter1 = 1

#collecting numbers from user
while counter1<=how_many_nums:
    x = int(input(f"Enter {counter1}. number--->>> "))
    list_of_the_nums.append(x)
    counter1 +=1
    
#sorting
list_of_the_nums.sort()

#printing the result
print(f"the biggest number is {list_of_the_nums[how_many_nums-1]}.")

print("See you")