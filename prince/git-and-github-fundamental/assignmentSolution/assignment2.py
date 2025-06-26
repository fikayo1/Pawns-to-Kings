# Question 1

# Ask user for first name and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
# print welcome message with the names
print(f"Hello {first_name}  {last_name}, welcome to python class!")


# Question 2

# Ask user to enter their age
age = int(input("Enter your age: "))
# check if user age is above 18
if age >= 18:
# print message accordingly
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# Question 3

# Ask for user input
number = int(input("Enter a number: "))


for i in range(13):
    result = number * i
    print(f"{number} X {i} = {result}")


# Question 4
# Ask user for starting number
starting_number = int(input("Enter a number to start countdown: "))
# while loop
while (starting_number >= 0):
    print(starting_number)
    starting_number -= 1
print("Blast off!")


# Question 5
# Ask user to enter q score between 0 and 100
# based on score, assign a grade
score = int(input("Enter your score: "))

message = "You've got a grade: "
if score >= 70 and score <=100:
    print(message, "A")
elif score >=60 and score <= 69:
    print(message, "B")
elif score >=50 and score <= 59:
    print("You've got a grade: C")
elif score >=40 and score <= 49:
    print("You've got a grade: D")
elif score >=0 and score <= 39:
    print("You've got a grade: F")


# Question 6:
# Ask user for number
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
    

# ask user for first number
first_number = float(input("Enter first number: "))
# ask user for operator
operator = input("Enter operator (+, -, *, /): ")
# ask user for second number
second_number = float(input("Enter second number: "))
# perform calculation
if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    print(first_number / second_number)
else:
    print("invalid operator")
# print result

# Question 8
# set secret number
secret_number = 9
# set counter
counter = 3
# set while loop
while counter > 0:
    guess = int(input("Guess the number (1-10): "))
# if correct print sucess
    if guess == secret_number:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong! Try again.")
    counter -=  1

