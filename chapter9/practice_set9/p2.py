import random

def game():
    print("You sre playing the game")
    score = random.randint(1,62)
    # Fetch the hiscore
    with open("Hiscore.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print(f"Your score : {score}")

    if score > hiscore:
    # write this high score to the file
       with open("Hiscore.txt","w") as f:
            f.write(str(score))
    return score

game()