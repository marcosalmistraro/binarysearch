low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guess_count = 1
while low != high:
    print("\tGuessing in the range {}:{}".format(low, high))
    guess = (high + low) // 2
    guess_hilow = input("My guess was {}, should I guess lower or higher? "
                        "Enter h or l, or c in case the answer was right"
                        .format(guess)).casefold()
    if guess_hilow == "h":
        low = (guess + 1)
        guess_count += 1
    elif guess_hilow == "l":
        high = (guess - 1)
        guess_count += 1
    elif guess_hilow == "c":
        print(f"The answer is {guess}. I got it in {guess_count} tries.")
        break
    else:
        print("Please enter an acceptable character: h, l or c")
        
print("You thought of the number {}".format(low))
print("I got it in {} tries".format(guess_count))
