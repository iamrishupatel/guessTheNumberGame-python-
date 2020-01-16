
# guess the secret number game 
# made by- Rishu Patel


from random import randint

# modify these statements if there is a change in range of random number or chances in Hard level
print("\t\t\t\t\tHint_ All numbers are less than 10,000\n") 
print("1: Normal (unlimited chances)\n2: Hard(20 chances)")

def play_again():
    #function that runs the game if user want to play it again.
    print("Do you want to play the game agiain?")
    choice = input("\n(Y/N): ") 

    if choice.lower() == 'y':
        main()
    else:
        None

def guess():
    # function to take input number from user
    try:
        guess_number = input("\nGuess the secret number>> ")
        if guess_number == 'q':
            quit()
        else:
            guess_number = int(guess_number)
    
    except ValueError:
        print("Please Enter a valid number.")
        return guess()
        
    else:
        return guess_number


def normal(secret_number):
    # Defining a function for normal level
    while True:
        guess_number = guess()
        if guess_number == secret_number:
            print("Congratulations You have guessed the secret number.\n")
            break

        elif guess_number > secret_number:
            print("Wrong Guess, It is smaller. Guess Again.")
        
        elif guess_number < secret_number:
            print("Wrong guess, It is bigger. Guess again.")
        

def hard(secret_number, chances):
    # Defining a function for hard level
    i = 1
    ch = chances
    print("You have",ch,"chances to guess the secret number.")

    while i <= ch:
        guess_number = guess()
        if guess_number == secret_number:
            print("Congratulations You have guessed the secret number.\n")
            break
        
        elif guess_number > secret_number:
            print("Wrong Guess, It is smaller. Guess Again.")
            print("You have",ch-i,"chances left.")
        
        elif guess_number < secret_number:
            print("Wrong guess, It is bigger. Guess again.")
            print("You have",ch-i,"chances left.")
        
        i +=1


def main():
    #main function to run the game.
    print("Enter 'q' at any point to quit.")
    try:
        level_select = input("Choose a level>>> ")
        if level_select == 'q':
            quit()
        else:
            level_select = int(level_select)
    
    except ValueError:
        print("Please choose a valid level.\n")
        main()
    
    else:
        secret_number = randint(1,10000)
        chances = 20  #select the number of chance for the hard level here,

        if level_select == 1:
            normal(secret_number)
        
        elif level_select == 2:
            hard(secret_number, chances)
        
        elif level_select == 'q':
            quit()

        else:
            print("Please choose a valid level.\n")
            main()
        
        play_again()
        


if __name__ == "__main__":
    main()
