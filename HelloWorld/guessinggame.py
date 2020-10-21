answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())
playing = True
while(playing):
    if guess == answer:
        print("You are right")
        playing = "false"
        break
    elif guess > answer:
        print("please guess lower")
        guess = int(input())
    else:
        print("please guess higher")
        guess = int(input())