# Question 1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Hello {first_name} {last_name}, welcome to Python class!")

#Question 2
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Question 3
number = int(input("Enter a number: "))
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#Question 4
start = int(input("Enter a starting number: "))
while start >= 0:
    print(start)
    start -= 1 

#Question 5
score = int(input("Enter your score (0–100): "))
if 70 <= score <= 100:
    print("Grade: A")
elif 60 <= score <= 69:
    print("Grade: B")
elif 50 <= score <= 59:
    print("Grade: C")
elif 40 <= score <= 49:
    print("Grade: D")
elif 0 <= score <= 39:
    print("Grade: F")
else:
    print("Invalid score. Please enter a number between 0 and 100.")

#Question 6
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Question 7
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please enter one of +, -, *, /.")

#Question 8
secret_number = 7
guess_count = 0
max_guesses = 3
while guess_count < max_guesses:
    guess = int(input("Guess the secret number (1-10): "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again.")
if guess != secret_number:
    print("Sorry, you've used all your guesses. The correct number was", secret_number)

#Question 9
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"The sum of the first {n} natural numbers is: {total}")

#Question 10
age = int(input("Enter your age: "))
if 0 <= age <= 12:
    print("You are a Child.")
elif 13 <= age <= 19:
    print("You are a Teenager.")
elif 20 <= age <= 64:
    print("You are an Adult.")
elif age >= 65:
    print("You are a Senior.")
else:
    print("Invalid age entered.")



