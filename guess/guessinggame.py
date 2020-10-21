import random

answer = random.randint(1, 10)
print(answer)
guess = int(input("Guess what number"))

while True:
    if answer == guess:
        print("You are right")
        playing = input("Do you want to play more?")
        if playing == "y" or playing == "yes":
            answer = random.randint(1, 10)
            print(answer)
            guess = int(input("Guess what number"))
        else:
            break
    elif answer > guess:
        print("guess higher")
        guess = int(input("Guess what number"))
    else:
        print("guess lower")
        guess = int(input("Guess what number"))
