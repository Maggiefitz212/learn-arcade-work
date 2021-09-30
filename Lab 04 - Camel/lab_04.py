import random


def main():
    # Print opening screen.
    print("Welcome to Lunch Money Larceny!")
    print("You have stolen lunch money from a kid to pay for your lunch.")
    print("The kid wants his lunch money back and is chasing you down! Get to the cafeteria")
    print("to spend the money and win!")

    done = False

    # Define starting variables
    feet_traveled = 0
    thirst = 0
    your_tiredness = 0

    kid_feet_traveled = -20
    drinks_left = 3
    distance_behind_you = feet_traveled - kid_feet_traveled

    # Create a while loop that will show the user the options
    while not done:
        print("A. Drink from your water bottle.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Sit in hallway and rest.")
        print("E. Status check.")
        print("Q. Quit.")

        # Get the user's choice
        user_input = input("What is your choice? ")
        if user_input.upper() == "Q":
            # Quit the game
            done = True
            print("You have quit the game. I understand.")
            print("It's probably because you don't want to steal money from children.")
        elif user_input.upper() == "E":
            # Give status update to user
            print("Feet traveled: " + str(feet_traveled))
            print("Drinks in canteen: " + str(drinks_left))
            print("The kid is " + str(distance_behind_you) + " feet behind you.")
        elif user_input.upper == "D":
            # User rested so tiredness is 0
            # Kid moves 7 - 14 feet closer
            your_tiredness = 0
            print("You are rested and ready to be a bully again.")
            kid_feet_traveled_in_round = random.randrange(7, 15)
            kid_feet_traveled = kid_feet_traveled + kid_feet_traveled_in_round
        elif user_input.upper() == "C":
            # Move ahead 10 - 20 feet at full speed
            # User gets a little more thirsty
            # User has a 1 in 20 chance of finding a water fountain
            # Kid moves forward 7 - 14 feet
            feet_traveled_in_round = random.randrange(10, 21)
            feet_traveled = feet_traveled + feet_traveled_in_round
            print("You have traveled " + str(feet_traveled_in_round) + " in this round.")
            print("You have traveled " + str(feet_traveled) + " total.")
            thirst = thirst + 1
            your_tiredness = your_tiredness + random.randrange(1, 4)
            kid_feet_traveled_in_round = random.randrange(7, 15)
            kid_feet_traveled = kid_feet_traveled + kid_feet_traveled_in_round
            water_fountain_chance = random.randrange(1, 21)
            if water_fountain_chance == 1 and not done:
                print("You have found a water fountain. Your water bottle is filled again!")
                thirst = 0
                your_tiredness = 0
                drinks_left = 3

        elif user_input.upper() == "B":
            # Move ahead 5 - 12 feet at moderate speed
            # User has a 1 in 20 chance of finding a water fountain
            # Kid moves forward 7 - 14 feet
            feet_traveled_in_round = random.randrange(5, 13)
            feet_traveled = feet_traveled + feet_traveled_in_round
            print("You have traveled " + str(feet_traveled_in_round) + " in this round.")
            print("You have traveled " + str(feet_traveled) + " in total.")
            water_fountain_chance = random.randrange(1, 21)
            if water_fountain_chance == 1 and not done:
                print("You have found a water fountain. Your water bottle is filled again!")
                thirst = 0
                your_tiredness = 0
                drinks_left = 3
        elif user_input.upper() == "A":
            # User takes a drink out of their water bottle
            # Their thirst is set to 0
            if drinks_left != 0:
                print("How refreshing! You aren't thirsty anymore!")
                thirst = 0

        if thirst > 6:
            # If statement checks to see if user passed out from dehydration and loses game
            print("You passed out from dehydration.")
            done = True
        elif thirst > 4:
            # If statement checks to see if user is getting close to passing out from dehydration
            # If true, it tells user that they are thirsty
            print("You are thirsty.")

        if your_tiredness > 8:
            # If statement checks to see if user passed out from exhaustion
            print("You passed out from exhaustion.")
        elif your_tiredness > 5:
            # If statement checks to see if user is getting close to passing out from exhaustion
            # If true, it tells user that they are thirsty
            print("You are getting tired.")

        if distance_behind_you <= 0:
            # This checks if kid has caught or passed user
            # If the kid has passed the user, it tells the user this and quits the game
            print("The kid caught you and took back his lunch money!")
            print("Not going to lie, I hoped this would happen. Thieves should be held accountable.")
            done = True
        elif distance_behind_you < 10:
            # This tells the user the kid is catching up if the kid is less than 10 feet away
            print("The kid's catching up!")

        if feet_traveled >= 200 and your_tiredness <= 8:
            # This tells the user they have won if their tiredness is less than or equal to 8
            # and they have traveled 200 or more feet
            print("You won! I feel bad for the kid though. You should give his money back.")


main()
