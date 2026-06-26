class Employee:
    company = "Microsoft"
    def show(self):
        print(f"Show Company {self.company}")
class Programmer(Employee):
    company = "ITC"
    language = "Python"
    def showLang(self):
        print(f"Show company {self.company} and language {self.language}")

b = Programmer()
b.show()
b.showLang()