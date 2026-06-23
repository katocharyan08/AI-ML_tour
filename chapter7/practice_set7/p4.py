num = int(input("Enter a number : "))
i = 2
if num <=1:
    print(f"{num} is not prime")
else:
   isPrime = True
while i*i < num:
    if num % i == 0:
        isPrime = False
        break
    i += 1
if isPrime == True:
    print(f"{num} is prime")
else:
    print(f"{num}is not prime")