class Calculator:
    def squareRoot(self):
        print(self.num**0.5)
    def square(self):
        print(self.num**2)
    def cube(self):
        print(self.num**3)
    def __init__(self,num):
        self.num = num

obj1 = Calculator(4)
obj1.square()
obj1.cube()
obj1.squareRoot()