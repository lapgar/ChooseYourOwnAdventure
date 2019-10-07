# background leading to the start needs to go up here

# ask for name and greet player
name = input("What is your name?")
print("\nHello " + name + "! \n")

# introduction to the game
print("Welcome to Sanctum! It is a land of magic and wonder, but be warned: darkness lurks in the corners.")

# Choice 1: fork in the road
print("There is a path in front of you and you decide to follow it. Eventually you reach a fork in the road.")
print("To the left is a field of flowers. To the right is a bridge over a river. \n")

# Omer taught me how to use a while loop
invalid = True
while invalid:
    choice1 = input("Do you go left or right?")

# went left
    if choice1 == "left":
        print("You walk to the " + choice1 + ".")
        print("The flowers smell lovely. \n")
        invalid = False
        print("As you walk your eyes grow heavy and your steps become more of a struggle.")
        print("You are about to collapse when suddenly a breeze clears your senses long enough to notice a patch of burnt flowers a dozen yards away. \n")
    # Choice 2:
        approach = True
        while approach:
            approachBurnt = input("Do you approach the burnt patch? 'yes' or 'no'")

        # approached burnt patch
            if approachBurnt == "yes":
                print("The edges of the patch are still smoldering, but your head is clear. \n")
                approach = False

        # did not approach burnt patch
            elif approachBurnt == "no":
                print("You pass out in the field. \n")
                approach = False
            else:
                print("Your indecisiveness in the face of danger is alarming, your vision grows hazy. \n")

# went right
    elif choice1 == "right":
        print("You walk to the " + choice1)
        print("As you approach the bridge you notice that a troll is blocking your path. \n")
        invalid = False
        print("The troll narrows his eyes at you and speaks in a surprisingly nasally voice.")
        print("'I haven't seen any humans come through here in a long time. Will you help me?' \n")
    # Choice 2: Help the Troll
        assist = True
        while assist:
            helpTroll = input("Will you help the troll? 'yes' or 'no'")

        # helped troll
            if helpTroll == "yes":
                print("His eyes mist over: he did not expect you to say yes. \n")
                assist = False

        # did not help troll
            elif helpTroll == "no":
                print("The troll nods his head sadly and steps aside, motioning for you to continue on your way. \n")
                assist = False
            else:
                print("Please give the troll a straightforward answer, he's had a long day. \n")
    elif choice1 == "back":
        print("You swear you saw a shadow disappearing into the trees. After a few moments of hesitation you decide to keep moving forward.")
        print("\n***********************\n")
    else:
        print("A creative response, but a deadly one. Please go either 'left' or 'right'.")
        print("\n***********************\n")
