#welcome the user to the game
print("********************************")
print("*                              *")
print("* WELCOME TO THE GUESSING GAME *")
print("*                              *")
print("********************************")

#import random number generator 

import random

#establish correct number

number = random.randint(1,100)

#print number for testing purposes only. comment out in production
# print(number)

#ask user for guess and store in a variable

guess = int(input("Give me a number between 1 and 100 : "))

#check if guess was correct and respond appropriately

if guess == number: 
    print("You got it! You're a genius.")
else:
    print("Nope. You lose.")