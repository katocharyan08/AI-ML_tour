class Employee:
    def __init__(self):
        print(" E Cons")
class Coder(Employee):
    def __init__(self):
        super().__init__()
        print(" C Cons")
class Programmer(Coder):
    def __init__(self):
        super().__init__()
        print(" p Cons")
x = Programmer()



