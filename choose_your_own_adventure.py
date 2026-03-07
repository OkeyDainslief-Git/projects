name = input("What is your name? ")
print("welcome", name, "to this adventure!")

answer = input("you are on a dirt road, it has come to an end and you can go left or right which way would you like to go? ").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim across? type walk to walk around and swim to swim across. ").lower()

    if answer == "swim":
        print("you swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game.")
    else:
        print("not a valid option. you lose.")

elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        print("you go back and lose.")
    elif answer == "cross":
        answer = input("you cross the bridge and meet the stranger. Do you talk to them (yes/no)? ").lower()

        if answer == "yes":
            print("you talk to the stranger and they give you gold. you win!")
        elif answer == "no":
            print("you ignore the stranger and keep walking. you lose.")
        else:
            print("not a valid option. you lose.")

    else:
        print("not a valid option. you lose.")

else:
    print("not a valid option. you lose.")

print("thank you for playing", name)
