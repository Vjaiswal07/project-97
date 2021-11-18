import random
print("number guessing game")
number=random.randint(1,9)
chances=0
print("guess a number between one and nine")
while chances<5:
    guess=int(input("enter your guess: "))
    if guess==number:
        print("congragulations you win")
        break
    elif guess<number:
        print("your guess was low, try a higher number")
    else:
        print("your guess was high, try a lower number")
    chances=chances+1
if not chances<5:
    print("you lose, the number is ",number)