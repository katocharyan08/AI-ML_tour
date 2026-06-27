class Employee:
    salary = 536237
    increment = 20
    @property
    def salaryAfterInc(self):
        return (self.salary + self.salary *(self.increment/100))
    @salaryAfterInc.setter
    def salaryAfterInc(self,salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee()
# print(e.salaryAfterInc)
e.salaryAfterInc = 280.8
print((e.increment))
