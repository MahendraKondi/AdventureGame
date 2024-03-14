name = input("Enter your name: ")
print("Welcome to adventure game!!",name)

while True:
    answer = input("You are on dirt road came to end you want to go left or right? ").lower()
    if answer == "left":
        wayy = input("Walking Walking river has came do u want to swim or goback? ").lower()
        if answer == "swim":
            print("You have jumped into river and you have dead.You lost the game")
            break
        elif answer == "goback":
            print("You can't go back and you have lost game")
            break
        else:
            print("Please try again:)")
    elif answer == "right":
        answer = input("Walking Walking a person came in the middle do u want to talk to him or not? talk/no? ").lower()
        if answer == "talk":
            print("Talking with him and he killed you and you lost the game")
            break
        elif answer == "no":
            print("You have won the game:)")
            break
        else:
            print("Please try again")
    else:
        print("Please try again:)")

print("Thank you for participating in the game")