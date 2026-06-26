class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self, other):
        return self.n + other.n

x = Number(3)
y = Number(5)
print(x + y)