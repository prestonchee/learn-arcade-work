"""
Preston Chee
02/02/2023
CS 1400
Camel Game
"""
import random

#main method
def main():
    print('Welcome to Camel!')
    print('You have stolen a camel to make your way across the great Mobi desert.')
    print('The natives want their camel back and are chasing you down! Survive your')
    print('desert trek and out run the natives.')

    #initiated variables
    done = False
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    canteen_amount = 3

    #main loop runs until done is true
    while not done:
        print('A. Drink from your canteen.')
        print('B. Ahead moderate speed.')
        print('C. Ahead full speed.')
        print('D. Stop for the night.')
        print('E. Status check.')
        print('Q. Quit.')

        #prompt for user choice
        user_choice = input('What is your choice')

        #run if loops for each choices made and the consequences of those choices
        if user_choice.upper() == 'Q':
            done = True
            print('Thanks for Playing ')
        elif user_choice.upper() == 'E':
            print('Mile Travel :', miles_traveled)
            print('Drinks in canteen:', canteen_amount)
            print('The natives are', miles_traveled - natives_distance, 'miles behind you')
            print(thirst)
        elif user_choice.upper() == 'D':
            camel_tiredness = 0
            print('The camel is happy')
            natives_distance += 8
        elif user_choice.upper() == 'C':
            miles_traveled += 14
            print('You have traveled', miles_traveled, 'miles')
            thirst += 1
            camel_tiredness += 3
            natives_distance += 9
            if random.randrange(19) == 7 and not done:
                print('You have found an Oasis! Canteen will be refilled')
                canteen_amount = 3
        elif user_choice.upper() == 'B':
            miles_traveled += 9
            print('You have traveled', miles_traveled, 'miles')
            thirst += 1
            camel_tiredness += 1
            natives_distance += 7
            if random.randrange(19) == 7 and not done:
                print('You have found an Oasis! Canteen will be refilled')
                canteen_amount = 3
        elif user_choice.upper() == 'A':
            if canteen_amount != 0:
                canteen_amount -= 1
                thirst = 0
                print('You have quenched your thirst')
            else:
                print('You have no water in your canteen')

        # create warning when you ar getting to thirsty
        if 6 >= thirst > 4:
            print('You are getting thirsty')
        elif thirst > 6:
            print('You have died of thrist')
            done = True

        # create warnings when camel is getting tired
        if 8 >= camel_tiredness > 5:
            print('Your camel is getting tired')
        elif camel_tiredness > 8:
            print('your camel has died to exhaustion')
            done = True

        # create warnings when getting to thirsty
        if natives_distance >= miles_traveled:
            print('You have been caught by the natives')
            done = True
        elif (miles_traveled - natives_distance) < 15:
            print('The natives are getting close!')
        elif miles_traveled >= 200 and not done:
            print('Congrats you have won the game and escaped from the natives')
            done = True




main()
