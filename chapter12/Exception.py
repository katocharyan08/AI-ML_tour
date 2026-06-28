# a = int(input("Enter a number : "))
# print(a)
# print("Thank you")
try:
    a = int(input("Enter a number : "))
    print(a)
except Exception as e:
    print(e)
print("Thank you")