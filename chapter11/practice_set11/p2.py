class Animals:
    print("All animals are not pet")

class Pets(Animals):
        print("Pets are the animal with friendly nature")

class Dog(Pets):
    @staticmethod
    def bark():
        print("Dog is barking : bhauu")

pillu = Dog()
pillu.bark()
