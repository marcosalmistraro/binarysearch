import random as rand

highest = 1000
answer = rand.randint(1,highest)
print(f"For test purposes - the answer is: {answer}")   # TODO Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input(""))
while guess != answer:
    if guess < answer:
        print("Please guess higher")
        guess = int(input(""))
    elif guess > answer:
        print("Please guess lower")
        guess = int(input(""))

print("Well done, you guessed it!")



