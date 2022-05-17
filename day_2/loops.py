#PART 1

# counter = 0
# my_number = 5

# while counter < my_number:
#     print("counter is " + str(counter))
#     counter = counter + 1
#     #counter += 1    /// += adds to the variable stated



#PART 2

# my_number = 5
# user_guess = int(input("What number between 1 and 9 am I thinking of?"))

# while user_guess != my_number:
#     #provide feedback whether the guess is too low or too high
#     if user_guess < my_number:
#         print("Your guess was too low!")
#     elif user_guess > my_number:
#         print("Your guess was too high!")
#     user_guess = int(input("Nope! Try again..."))

# print("Well done, you got it!")



#PART 3

# while True:
#     line = input("Type something: ")

#     if line == "q":
#         break
    
#     #print("You typed " + line) #concatenation
#     print(f"You typed {line}") #interpolation



#PART 4

#numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number * 100)

##multiply all numbers by 100 and print

# total = 0

# for number in numbers:
#     total += number

# #Add all the numbers to find the total

# print(total)



#PART 5

chickens = [
  {"name": "Margaret", "age": 2, "eggs": 0},
  {"name": "Hetty", "age": 1, "eggs": 2},
  {"name": "Henrietta", "age": 3, "eggs": 1},
  {"name": "Audrey", "age": 2, "eggs": 0},
  {"name": "Mabel", "age": 5, "eggs": 1}
]

# for chicken in chickens:
#     #Print something like 'Margaret is 2'
#     #print(chicken["name"] + " is " + str(chicken["age"]))
#     print(f'{chicken["name"]} is {chicken["age"]}')

##interpolation string inside a string - requires use of ' and ""

total_eggs = 0

for chicken in chickens:
    #total_eggs = total_eggs + chicken["eggs"]
    total_eggs += chicken["eggs"]
    chicken["eggs"] = 0

print(f"{total_eggs} eggs collected")

for chicken in chickens:
    print(chicken)


for chicken in chickens:
    if chicken["eggs"] > 0:
        print("wooo eggs!")