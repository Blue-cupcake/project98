import random

print("Number Guessing Game")
print("Guess a number between 1-10")
print("You will get 5 chances until you guess it right!!")
number=random.randint(1,10)
print(number)
guess=int(input("Enter your guess:-"))
if (number)==(guess):
    print("Yay you got it right!!") 
else:
    print("Uh!Oh!Try again")
    guess2=int(input("Enter your 2nd guess:-"))


if (number)==(guess2):
    print("Yay you got it right!!")
else:
    print("Uh!Oh!Try again")
    guess3=int(input("Enter your 3rd guess:-"))

if (number)==(guess3):
    print("Yay you got it right!!")
else:
    print("Uh!Oh!Try again")
    guess4=int(input("Enter your 4th guess:-"))    

if (number)==(guess4):
    print("Yay you got it right!!")
else:
    print("Uh!Oh!Try again")
    guess5=int(input("Enter your 5th guess:-"))        

if (number)==(guess5):
    print("Yay you got it right!!")
else:
    print("You lose :(")    