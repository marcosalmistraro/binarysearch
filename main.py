import random as rand

highest = 1000
answer = rand.randint(1, highest)

guess = int(input(("Please guess a number between 1 and {}: ".format(highest))))

tries_count = 0
while guess != answer:
    if guess < answer:
        guess = int(input("Please guess higher"))
        tries_count += 1
    elif guess > answer:
        guess = int(input("Please guess lower"))
        tries_count += 1

print("Well done, you guessed it in {} tries!".format(tries_count))
