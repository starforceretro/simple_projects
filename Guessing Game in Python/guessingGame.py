import random # This will allow us to generate random numbers

randomNumber = random.randint(1, 20) # This will generate a random number between 1 and 20
correctGuess = False # This will make it so correctGuess is FALSE at the beginning of the program

print("Hello! Welcome to my number guessing game!") # print welcome text
print("A number between 1 and 20 will be generated.")
print("Do you have what it takes?")

while not correctGuess: # This will run while correctGuess is false, the loop will stop when correctGuess is true
    guess = int(input("Please enter your guess: ")) # This will get the user's guess 

    if guess < randomNumber: # This If statement will check to see if the users guess is too low
        print("That is too low! Please try again!")
    
    elif guess > randomNumber: # This elif statement will check to see if the users guess is too high
        print("That is too high! Please try again!")

    else: # We have used a else statement instead of If guess == randomNumber because it is more efficent. There can't be anything other than too high or low
        print("Well done! The correct number was indeed " + str(randomNumber)) # this will tell the user they guessed the random number correctly
        correctGuess = True  # This will break the loop, making correctGuess true


print("You have beaten my number guessing game!") # This will tell the user they have sucessfully beat the game
