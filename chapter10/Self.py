class Employee:

    language = "Python"
    salary = 4444400

    def getInfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")
obj1 = Employee()
obj1.name = "Roro nova zoro"

# 1st way to call

obj1.getInfo()

# 2nd way to call

Employee.getInfo(obj1)