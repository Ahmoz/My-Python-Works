def factorialCalculate(x):
    result = 1
    if x == 0:
        return 1
    if x <0:
        return "you cannot calculate factorial with negative numbers"
    while x > 1:
        result *= x
        x -=1
    return result



print(factorialCalculate(-1))