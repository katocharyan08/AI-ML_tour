class Employee:

    language = "Python"
    salary = 4444400

    def __init__(self):
        print("KAlu verr")
    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary

obj1 = Employee("Roro nova zoro","japnese",121444414)
print(obj1.name,obj1.language,obj1.salary)

