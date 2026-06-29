a = int(input("Enter 1st Number : "))
b = int(input("Enter 2nd Number : "))
c = int(input("Enter 3rd Number : "))
d = int(input("Enter 4th Number : "))

if(a<b and a<c and a<d):
    ans = a
elif(b<c and b<d):
    ans = b
elif(c<d):
    ans = c
else:
    ans = d
tr
print("Answer is ", ans)