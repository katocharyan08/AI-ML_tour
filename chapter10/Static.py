class Employee:

    language = "Python"
    salary = 4444400

    @staticmethod
    def greet():
        print("Good")

obj = Employee()
obj.greet()
Employee.greet()