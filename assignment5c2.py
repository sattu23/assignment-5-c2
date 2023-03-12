# Challenge 2 implement a calculator class>>

class calculator:
    
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def add(self):
        return(self.num2+self.num1)
    def subtract(self):
        return(self.num2-self.num1)
    def multiply(self):
        return(self.num2*self.num1)
    def divide(self):
        return(self.num2/self.num1)
num1=int(input('enter num1>>'))
num2=int(input('enter num2>>'))
output=calculator(num1,num2)
print('addition>>',output.add())
print('subtraction>>',output.subtract())
print('multiplication>>',output.multiply())
print('division>>',output.divide())


