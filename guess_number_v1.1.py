print("I'm thinking about a number! try to guess")
secretNumber = 12453
guessNumber = 0
while guessNumber != secretNumber:
    guessNumber = int(input("the secret number: "))
    if guessNumber > secretNumber:
        if guessNumber > (secretNumber + 2000):
            print("its much smaller! guess")
        else:
            print("It's bit smaller! guess")
    elif guessNumber < secretNumber:
        if guessNumber < (secretNumber - 2000):
            print("its much bigger! guess")
        else:
            print("It's bit bigger! guess")
    else:
        print("Congratulations You guessed it right")
