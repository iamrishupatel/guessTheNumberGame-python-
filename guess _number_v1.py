#Guess Number

secretNumber = 56
guessNumber = 0
while guessNumber != secretNumber:
    guessNumber = int(input("Tell me your number: "))
    if (guessNumber == secretNumber):
        print("You guessed the secret number :)")
    else:
        print("Your guess is wrong please guess again :( ")
