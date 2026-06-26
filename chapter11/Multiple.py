class Employee:
    company = "Microsoft"
    def show(self):
        print(f"Show Company {self.company}")
class Coder:
    language = "kala"
    def demo(self):
        print(f"Show demo language {self.language}")
class Programmer(Employee,Coder):
    company = "ITC"
    language = "Python"
    def showLang(self):
        print(f"Show company {self.company} and language {self.language}")

b = Programmer()
b.show()
b.showLang()
b.demo()

c = Coder()
c.demo()