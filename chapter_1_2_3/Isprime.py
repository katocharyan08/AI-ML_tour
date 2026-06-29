n = int(input("Enter Number : "))
if n <= 1:
    is_prime = False
else:
    is_prime = True  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if(is_prime):
    print("The number is prime")
else:
    print("The number is not prime")