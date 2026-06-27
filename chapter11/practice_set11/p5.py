class Vector:
    def __init__(self,l):
        self.l = l
    def __len__(self):
        return len(self.l)

x = Vector([1,2,3,4])
print(len(x))