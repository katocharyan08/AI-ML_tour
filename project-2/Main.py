# Perfect Guess
from random import randint

n = randint(1,100)
print("--Guess the number Game--".upper())
a = -1
guesses = 1
while a != n:
    a = int(input("Guess : "))
    if a < n:
        print("Go Higher")
        guesses += 1

    elif a > n:
        print("Go Lower")
        guesses += 1

print(f"The number {n} is guessed in {guesses} attempts")
