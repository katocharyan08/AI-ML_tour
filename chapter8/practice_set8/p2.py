def conersion(celsius):
    return (celsius * 9/5) + 32

celsius = int(input("Enter  celsius degree : "))
a = conersion(celsius)
print(f"{celsius}C is {a}F")