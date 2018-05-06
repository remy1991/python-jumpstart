import random

print("-------------------------------------------------")
print("               Guess the number")
print("-------------------------------------------------")
print()

the_number = random.randint(0, 100)
guess = -1
name = input("Please enter your name: ")

while guess != the_number:
    guess_text = input("Guess the number between 0 to 100: ")
    guess = int(guess_text)
    if guess < the_number:
        print("Too low")
        print("Sorry {}, your guess of {} was too LOW".format(name,guess))
    elif guess > the_number:
        print("Sorry {}, your guess of {} was too HIGH".format(name,guess))
    else:
        print("Hey {}, you won, {} it is!".format(name,guess))

print("Done")