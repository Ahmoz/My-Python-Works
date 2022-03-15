def gradeCalculator(midterm,final,midterm_percentage):
    grade = ((midterm*midterm_percentage)+(final*(100-midterm_percentage)))/100
    return grade
    
