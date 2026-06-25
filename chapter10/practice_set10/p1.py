from platform import system_alias


class Programmer:
    company = "Microsoft"
    def __init__(self,name,id,department,salary):
        self.name = name
        self.id = id
        self.department = department
        self.salary = salary
obj1 = Programmer("Aryan",101,"Software development",350000)
obj2 = Programmer("Arun",102,"Web Dev",450000)
obj3 = Programmer("kamo",103,"AI/ML",4566788)
print(obj1.name,obj1.id,obj1.department,obj1.salary,obj1.company)
print(obj2.name,obj2.id,obj2.department,obj2.salary,obj2.company)
print(obj3.name,obj3.id,obj3.department,obj3.salary,obj3.company)