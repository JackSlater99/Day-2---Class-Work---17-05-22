guess = input("What year was python created? ")
if not guess.isnumeric():
    print("That is not a number")
elif int(guess) == 1991:
    print("Correct!")
else:   
    print("Better luck next time.")