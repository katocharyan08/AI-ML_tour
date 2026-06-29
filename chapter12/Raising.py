a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

if b == 0:
    raise ZeroDivisionError("Our program is not meant to be divide by zero")
else:
    print(f"The divison of a/b is {a/b}")