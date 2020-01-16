#Guess the nuber game v3
#Created by Rishu Patel on June 30th 2019 | 1:10 AM
 
print("THIS GAME HAS 10 SECRET NUMBERS") #you can add as many numbers as you want
print("I'm thinking about a number!")
secret_numbers = (874, 3263, 2154, 10, 698, 782, 9863, 214, 985, 3232) #we added a tuple of secret numbers to guess
guess_number = 0
for secret_number in secret_numbers:
    while guess_number != secret_number:
        guess_number = int(input("Try to guess the secret number: ")) #taking input from user
        #checking if number is smaller or bigger than secret number
        if guess_number > secret_number:
            if guess_number > (secret_number + 2000):
                print("its much smaller!")
            else:
                print("It's bit smaller!")
        elif guess_number < secret_number:
            if guess_number < (secret_number - 2000):
                print("its much bigger!")
            else:
                print("It's bit bigger!")
        else:
            print("Congratulations You guessed it")

 #taking input from the user again if he want to play the game again or not 
    play_again = input("Do you want to play again?(y/n): ")
    if play_again == "n":
         break
         
            
