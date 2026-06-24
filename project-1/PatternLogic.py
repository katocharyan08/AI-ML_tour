import random

computer = random.choice([1,-1,0])
youstr = input("Enter your choice : ")
youDict = {
           "s" : 1,
            "w" : -1,
            "g" : 0
          }
reverseDict = {
                1 : "Snake",
                -1 : "Water",
                0 : "Gun"
            }
you = youDict[youstr]

print(f"Your choice : {reverseDict[you]} \nComputer choice : {reverseDict[computer]}")
'''

if computer == -1 and you == 1: (c - y) = -2
    print("You Win")
elif computer == -1 and you == 0: (c - y) = -1
    print("You Loss")
elif computer == 1 and you == -1: (c - y) = 2
    print("You Loss")
elif computer == 1 and you == 0: (c - y) = 1
    print("You Win")
elif computer == 0 and you == -1: (c - y) = 1
    print("You Win")
elif computer == 0 and you == 1: (c - y) = -1
    print("You Loss")
else:
    print("Something wrong")
'''
if computer == you:
    print("Draw")
elif (computer - you) == 1 or (computer - you) == -2:
    print("You Win")
else:
    print("You loss")
