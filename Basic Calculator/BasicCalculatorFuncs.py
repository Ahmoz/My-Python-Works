class Operations:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def summation(self):
        return self.num1 + self.num2
    
    def extraction(self):
        return self.num1 - self.num2
    
    def production(self):
        return self.num1 * self.num2
    
    def division(self):
        if(self.num2==0):
            return ("you cannot divide a number by 0")
        return self.num1 / self.num2
    
    