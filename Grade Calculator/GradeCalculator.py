import GradeFuncs as gf


print("Welcome to Grade Calculator!!")
print("******************************")

midterm = float(input("Midterm ->>>"))

while(midterm<0 or midterm>100):
    print("You entered invalid midterm!!")
    midterm = float(input("Midterm ->>>"))

midterm_perc = float(input("Midterm Percentage"))

while(midterm_perc<0 or midterm_perc>100):
    print("You entered invalid midterm percentage!!")
    midterm_perc = float(input("Midterm Percentage ->>>"))


final = float(input("Final -->>>"))

while(final<0 or final>100):
    print("You entered invalid Final")
    final = float(input("Final ->>>"))
    

grade = gf.gradeCalculator(midterm, final, midterm_perc)

print(f"Your grade is {grade}.")