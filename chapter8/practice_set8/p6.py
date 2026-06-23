def conersion(inches):
    return inches * 2.54

inches = int(input("Enter inches : "))
a = conersion(inches)
print(f"{inches} inches is {a} cm")