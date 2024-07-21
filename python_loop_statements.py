
import random


days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(days_of_week[::2]) # Print every second day of the week

#------------------------------------------------------------------------#

while True:  
    answer = input("What is the secret password to exit? ")

    if answer == "exit":  
        print("Congratulations! You've found the way out!")
        break  
    else:
        print("Nope, try again!")
#-------------------------------------------------------------------------#
coffie_shop = []

while len(coffie_shop) < 5:
    print("Still seats available at high top bar.")
    coffie_shop.append('person')
    print("There are", len(coffie_shop), "people currently sitting at the hightop bar area")

print(coffie_shop) 

#-------------------------------------------------------------------------#

#extra credit assignement
import random

items = ["cell phone", "laptop", "keyboard", "mouse", "headphones"]
secret_item = random.choice(items)
print("Welcome to the guessing game! You have an item that you need more then anythning else to be a software engineer! What is your guess?")


while True:
    guess = input()

    if guess == secret_item:
        print("Congratulations! You've guessed correctly!")
        break
    else:
        if guess in secret_item:
            print("Your guess is close, but it's not the item. Try again!")
        else:
            print("Sorry, that item is not even on the list...come on bro!")
        print("Try again! You can do it!")

#---------------------------------------------------------------#




