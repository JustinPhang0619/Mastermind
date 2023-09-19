import random
from logging import shutdown

#Introduction to the game
def intro():
    print("==============================================================================================")
    print("--------------------------------Welcome to the Mastermind Game--------------------------------" )
    print("==============================================================================================\n")
    print("------------------------------------------Intructions-----------------------------------------")
    print("1. This is a colour guessing game.")
    print("2. There are 6 colours in this game: ")
    print("   Red (R), Green (G), Blue (B), Yellow (Y), White (W), Pink (P)")
    print("3. Your goal is to guess all 4 colours in a random list correctly.")
    print("4. The game will tell you the number of colours that are in the right position each attempt.")
    print("5. The game will end once you have correctly guessed all the colours in the correct position.\n")
    print("---------------------------------------------Rules--------------------------------------------")
    print("1. You are required to only type in the colour code for each colour.")
    print("   Example: R for Red.")
    print("2. You will lose if you do not win within 10 attempts.\n")
    ready()

#Asking the player if they are ready or not
def ready():
    print("Are you ready to play?")
    ready_or_not = input("Enter Y if you are ready and N if you are not ready: ").upper()
    if ready_or_not == "Y":
        print("The game shall begin.\n")
        start()
    elif ready_or_not == "N":
        print("Understood. Have a nice day!")
        exit()
    else:
        print("Invalid input. Please enter Y to start the game or N to exit the game.\n")
        ready()

#Starting the game and generating the list
def start():
    colour_list=["R","G", "B", "Y", "W", "P"]
    random_list=[]
    attempt = 0
    counter = 0
    left = 10
    while counter < 4:
        random_list.append(random.choice(colour_list))
        counter = counter + 1

    #Only for demonstration (Giving the answer, you may delete the # below if you want a demo)
    #print("This is the random list: " + str(random_list) + (" (Only for the demo) ") )

    #Allowing ten attempts to the player
    while attempt < 10:
        invalid_num = 0
        correct = 0
        position = 0
        dupe_rand = []
        dupe_guess = []

        print("These are the available colours: Red (R), Green (G), Blue (B), Yellow (Y), White (W), Pink (P)")
        guess = input("Enter your colour guess: ").upper()
        attempt = attempt + 1
        left = left - 1
        
        #Prompt error if the player does not enter 4 colours
        if len(guess) != len(random_list):
            print("Please enter 4 colours next time!\n")
            continue
        
        #Prompt error if the player does not enter the colour that is in the list given
        for i in range(len(guess)):
            if guess[i] not in colour_list:
                invalid_num = invalid_num + 1
        
        if invalid_num >= 1:
            print("Invalid colour detected!")
            print("Number of invalid colour detected = " + str(invalid_num))
            print("Please Enter Red (R), Green (G), Blue (B), Yellow (Y), White (W) and Pink (P) next time.\n")

        #Counting number of correct colours
        for i in range(len(guess)):
            if guess[i] == random_list[i]:
                correct = correct + 1

        #Counting the number of correct but misplaced colours
        for i in range(len(guess)):
            if guess[i] in random_list and guess[i] != random_list[i]:
                dupe_rand.append(random_list[i])
                dupe_guess.append(guess[i])

        for i in range(len(dupe_rand)):
            if dupe_guess[i] in dupe_rand:
                position = position + 1 
                for j in range(len(dupe_rand)):
                    if dupe_rand[j] == dupe_guess[i]:
                        dupe_rand[j] = "x"
        
        #Win screen
        if correct == 4:
            print("==============================================================================================")
            print("=========================================YOU WON==============================================")
            print("==============================================================================================\n")
            print("The answer was " + str(random_list))
            print("Number of attempts: " + str(attempt))
            again()

        #Telling the users the attempts left and the number of correct guesses
        else:
            print("Your guess was wrong.")
            print("Number of correct guesses: " + str(correct))
            print("Number of correct but misplaced colours: "+ str(position))
            print("Please try again.")
            print("You have attempted "+ str(attempt) + " time(s)")
            print("You have " + str(left) + " attempt(s) left\n")
    print("You have lost the game!")
    again()

#Asking whether the players wants to play again or not
def again():
    print("Would you like to restart the game?")
    ready_or_not = input("Enter Y if you want to play again and N if you want to exit the game: ").upper()
    if ready_or_not == "Y":
        print("The game shall begin.\n")
        start()
    elif ready_or_not == "N":
        shut_down()
    else:
        print("Invalid input. Please enter Y to start the game or N to exit the game.\n")
        ready()   

#Shut down
def shut_down():
    print("==============================================================================================")
    print("====================================THANK YOU FOR PLAYING=====================================")
    print("==============================================================================================\n")
    quit() 

intro()
