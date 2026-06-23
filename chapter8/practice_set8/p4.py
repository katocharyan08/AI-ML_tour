def sum(n):
    if(n < 1):
        return 0
    if(n == 1):
      return 1
    return n + sum(n-1)
n = int(input("Enter a number : "))
a = sum(n)
print(a)