name = input("What is your name? ")
print("Welcome", name, "to this adventure!")

answer = input("You are at a crossroad. Do you want to go left or right? ").lower()
if answer == "left":
    answer = input("You come to a lake. Do you want to [swim] across or [wait] for a boat? ").lower()
    if answer != "swim" and answer != "wait":
        answer = input("Do you want to swim or wait? ").lower()
        if answer == "wait":
            answer = input("You arrive at an island with a house with 3 doors: red, yellow, and blue. Which color do you choose? ").lower()
            if answer == "yellow":
                print("You found the treasure! You win!")
            elif answer == "red":
                print("You were burned by fire. Game over.")
            elif answer == "blue":
                print("You were eaten by beasts. Game over.")
            else:
                print("You chose a door that doesn't exist. You've become trapped between realities, drifting in a void forever.")
    elif answer == "wait":
        answer = input("You arrive at an island with a house with 3 doors: red, yellow, and blue. Which color do you choose? ").lower()
        if answer == "yellow":
            print("You found the treasure! You win!")
        elif answer == "red":
            print("You were burned by fire. Game over.")
        elif answer == "blue":
            print("You were eaten by beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You were attacked by trout. Game over.")
else:
    print("You fell into a hole. Game over.")
