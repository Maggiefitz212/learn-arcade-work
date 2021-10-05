import random


def main():
    print("Welcome to Lunch Money Larceny!")
    print("You have stolen lunch money from a kid to pay for your lunch.")
    print("The kid wants his lunch money back and is chasing you down! Get to the cafeteria")
    print("to spend the money and win!")

    done = False

    feet_traveled = 0
    thirst = 0
    your_tiredness = 0

    kid_feet_traveled = -20
    drinks_left = 3
    distance_behind_you = feet_traveled - kid_feet_traveled

    while not done:
        print("A. Drink from your water bottle.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Sit in hallway and rest.")
        print("E. Status check.")
        print("Q. Quit.")

        user_input = input("What is your choice? ")
        if user_input.upper() == "Q":
            done = True
            print("You have quit the game. I understand.")
            print("It's probably because you don't want to steal money from children.")
        elif user_input.upper() == "E":
            print("Feet traveled: " + str(feet_traveled))
            print("Drinks in canteen: " + str(drinks_left))
            distance_behind_you = feet_traveled - kid_feet_traveled
            print("The kid is " + str(distance_behind_you) + " feet behind you.")
        elif user_input.upper() == "D":
            your_tiredness = 0
            print("You are rested and ready to be a bully again.")
            kid_feet_traveled_in_round = random.randrange(7, 15)
            kid_feet_traveled = kid_feet_traveled + kid_feet_traveled_in_round
            distance_behind_you = feet_traveled - kid_feet_traveled
            if distance_behind_you > 0:
                print("The kid is " + str(distance_behind_you) + " feet behind you.")
        elif user_input.upper() == "C":
            feet_traveled_in_round = random.randrange(10, 21)
            feet_traveled = feet_traveled + feet_traveled_in_round
            print("You have traveled " + str(feet_traveled_in_round) + " in this round.")
            print("You have traveled " + str(feet_traveled) + " total.")
            thirst = thirst + 1
            your_tiredness = your_tiredness + random.randrange(1, 4)
            kid_feet_traveled_in_round = random.randrange(7, 15)
            kid_feet_traveled = kid_feet_traveled + kid_feet_traveled_in_round
            distance_behind_you = feet_traveled - kid_feet_traveled
            if distance_behind_you > 0:
                print("The kid is " + str(distance_behind_you) + " feet behind you.")
            water_fountain_chance = random.randrange(20)
            if water_fountain_chance == 1:
                print("You have found a water fountain. You refilled your water bottle.")
                your_tiredness = 0
                drinks_left = 3
                thirst = 0
        elif user_input.upper() == "B":
            feet_traveled_in_round = random.randrange(5, 13)
            feet_traveled = feet_traveled + feet_traveled_in_round
            print("You have traveled " + str(feet_traveled_in_round) + " in this round.")
            print("You have traveled " + str(feet_traveled) + " in total.")
            kid_feet_traveled_in_round = random.randrange(7, 15)
            kid_feet_traveled = kid_feet_traveled + kid_feet_traveled_in_round
            distance_behind_you = feet_traveled - kid_feet_traveled
            if distance_behind_you > 0:
                print("The kid is " + str(distance_behind_you) + " feet behind you.")
            water_fountain_chance = random.randrange(20)
            if water_fountain_chance == 1:
                print("You have found a water fountain. You refilled your water bottle.")
                your_tiredness = 0
                drinks_left = 3
                thirst = 0
        elif user_input.upper() == "A":
            if drinks_left != 0:
                thirst = 0
                print("That's refreshing! You aren't thirsty anymore.")
            else:
                print("You are out of water!")
                print("You passed out from dehydration.")
            kid_feet_traveled_in_round = random.randrange(7, 15)
            kid_feet_traveled = kid_feet_traveled + kid_feet_traveled_in_round
            distance_behind_you = feet_traveled - kid_feet_traveled
            if distance_behind_you > 0:
                print("The kid is " + str(distance_behind_you) + " feet behind you.")
        if thirst > 6:
            print("You passed out from dehydration.")
            done = True
        elif thirst > 4:
            print("You are thirsty.")

        if not done:
            if your_tiredness > 8:
                print("You passed out from exhaustion.")
                done = True
            elif your_tiredness > 5:
                print("You are getting tired.")

        if not done:
            if distance_behind_you <= 0:
                print("The kid caught you and took back his lunch money!")
                print("Not going to lie, I hoped this would happen. Thieves should be held accountable.")
                done = True
            elif distance_behind_you < 15:
                print("The kid's catching up!")

        if not done:
            if feet_traveled >= 200 and your_tiredness <= 8:
                print("You won! I feel bad for the kid though. You should give his money back.")


main()
