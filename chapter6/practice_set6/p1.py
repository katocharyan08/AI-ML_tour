a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))
d = int(input("Enter 4th number : "))

if a>b and a>c and a>d :
    print("a is greater")
elif b>c and b>d :
    print("b is greater")
elif c>d :
    print("c is greater")
else :
    print("d is greater")