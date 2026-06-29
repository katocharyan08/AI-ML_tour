a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter another number: "))
if a >= b and a >= c:
    print("largest num ",a)
elif b >= a and b >= c:
    print("largest num ",b)
elif c >= a and c >= b:
    print("largest num ",c)

if a <= b and a <= c:
    print("samllest num ",a)
elif b <= a and b <= c:
    print("samllest num ",b)
elif c <= a and c <= b:
    print("samllest num ",c)

