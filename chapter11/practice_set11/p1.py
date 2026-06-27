class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"Show 2D vector coordinates : {self.i,self.j}")


class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"Show 3D vector coordinates : {self.i,self.j,self.k}")

x = ThreeDVector(2,4,7)
x.show()
y = TwoDVector(2,6)
y.show()