class Employee:
    a = 3
class Coder(Employee):
    b = 5
class Programmer(Coder):
    c = 6
x = Programmer()
print(x.a + x.b + x.c)
