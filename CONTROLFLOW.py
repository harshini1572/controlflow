#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#BASIC IF-ELSE


# In[3]:


#Q1. Write a Python program to check if a given number is positive or negative.

num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# In[4]:


#Q2. Create a program that determines if a person is eligible to vote based on their age.

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# In[6]:


#Q3. Develop a program to find the maximum of two numbers using if-else statements.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print("The maximum number is", num1)
else:
    print("The maximum number is", num2)


# In[ ]:


#Q4. Write a Python script to classify a given year as a leap year or not.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")


# In[ ]:


#Q5. Create a program that checks whether a character is a vowel or a consonant.

char = input("Enter a character: ").lower()
if char in 'aeiou':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")


# In[ ]:


#Q6. Implement a program to determine whether a given number is even or odd.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# In[ ]:


#Q7. Write a Python function to calculate the absolute value of a number without using the abs() function.

def absolute_value(num):
    if num < 0:
        return -num
    else:
        return num

number = float(input("Enter a number: "))
print("The absolute value is", absolute_value(number))


# In[ ]:


#Q8. Develop a program that determines the largest of three given numbers using if-else statements.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is", num2)
else:
    print("The largest number is", num3)


# In[ ]:


#Q9. Create a program that checks if a given string is a palindrome.

string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# In[ ]:


#Q10. Write a Python program to calculate the grade based on a student's score.

score = float(input("Enter the score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# In[7]:


##Nested If-Else Statements


# In[ ]:


#Q11. Write a program to find the largest among three numbers using nested if-else statements.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2:
    if num1 >= num3:
        print("The largest number is", num1)
    else:
        print("The largest number is", num3)
else:
    if num2 >= num3:
        print("The largest number is", num2)
    else:
        print("The largest number is", num3)


# In[ ]:


#Q12. Implement a program to determine if a triangle is equilateral, isosceles, or scalene.

side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if side1 == side2:
    if side2 == side3:
        print("The triangle is equilateral.")
    else:
        print("The triangle is isosceles.")
else:
    if side2 == side3 or side1 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")


# In[ ]:


#Q13. Develop a program that checks if a year is a leap year and also if it is a century year.

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is a leap year and a century year.")
        else:
            print("The year is a century year but not a leap year.")
    else:
        print("The year is a leap year but not a century year.")
else:
    print("The year is not a leap year.")


# In[ ]:


#Q14. Write a Python script to determine if a number is positive, negative, or zero.

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# In[ ]:


#Q15. Create a program to check if a person is a teenager (between 13 and 19 years old).

age = int(input("Enter your age: "))

if 13 <= age <= 19:
    print("The person is a teenager.")
else:
    print("The person is not a teenager.")


# In[ ]:


#Q16. Develop a program that determines the type of angle based on its measure (acute, obtuse, or right).

angle = float(input("Enter the angle in degrees: "))

if angle < 90:
    print("The angle is acute.")
elif angle == 90:
    print("The angle is right.")
elif angle > 90 and angle < 180:
    print("The angle is obtuse.")
else:
    print("The angle is not valid (should be less than 180 degrees).")


# In[ ]:


#Q17. Write a Python program to calculate the roots of a quadratic equation.

import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = cmath.sqrt(b**2 - 4*a*c)

root1 = (-b + discriminant) / (2*a)
root2 = (-b - discriminant) / (2*a)

print("The roots are", root1, "and", root2)


# In[ ]:


#Q18. Implement a program to determine the day of the week based on a user-provided number (1 for Monday, 2 for Tuesday, etc.).

day = int(input("Enter a number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input. Enter a number between 1 and 7.")


# In[ ]:


#Q19. Create a program that determines if a year is a leap year and also if it is evenly divisible by 400.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("The year is a leap year and is divisible by 400.")
elif year % 4 == 0:
    print("The year is a leap year but not divisible by 400.")
else:
    print("The year is not a leap year.")


# In[ ]:


#Q20. Develop a program that checks if a given number is prime or not using nested if-else statements.

num = int(input("Enter a number: "))

if num > 1:
    if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
        print("The number is prime.")
    else:
        print("The number is not prime.")
else:
    print("The number is not prime.")


# In[8]:


##Elif Statements:


# In[ ]:


#Q21. Write a Python program to assign grades based on different ranges of scores using elif statements.

score = float(input("Enter the score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# In[ ]:


#Q22. Implement a program to determine the type of a triangle based on its angles.

angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

if angle1 + angle2 + angle3 == 180:
    if angle1 < 90 and angle2 < 90 and angle3 < 90:
        print("The triangle is acute.")
    elif angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("The triangle is right.")
    else:
        print("The triangle is obtuse.")
else:
    print("The angles do not form a valid triangle.")


# In[ ]:


#Q23. Develop a program to categorize a given person's BMI into underweight, normal, overweight, or obese 
# using elif statements.

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height**2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("Obese")


# In[ ]:


#Q24. Create a program that determines whether a given number is positive, negative, or zero using elif statements.

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# In[ ]:


#Q25. Write a Python script to determine the type of a character (uppercase, lowercase, or special) using elif statements.

char = input("Enter a character: ")

if char.isupper():
    print("The character is uppercase.")
elif char.islower():
    print("The character is lowercase.")
else:
    print("The character is special.")


# In[ ]:


#Q26. Implement a program to calculate the discounted price based on different purchase amounts using elif statements.

amount = float(input("Enter the purchase amount: "))

if amount >= 1000:
    discount = 0.2
elif amount >= 500:
    discount = 0.1
elif amount >= 100:
    discount = 0.05
else:
    discount = 0

discounted_price = amount * (1 - discount)
print("The discounted price is", discounted_price)


# In[ ]:


#Q27. Develop a program to calculate the electricity bill based on different consumption slabs using elif statements.

units = float(input("Enter the number of units consumed: "))

if units <= 100:
    bill = units * 1.5
elif units <= 300:
    bill = units * 3
elif units <= 500:
    bill = units * 5
else:
    bill = units * 7

print("The electricity bill is", bill)


# In[ ]:


#Q28. Create a program to determine the type of quadrilateral based on its angles and sides using elif statements.

angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))
angle4 = float(input("Enter the fourth angle: "))

if angle1 + angle2 + angle3 + angle4 == 360:
    if angle1 == angle2 == angle3 == angle4:
        print("The quadrilateral is a square.")
    elif angle1 == angle3 and angle2 == angle4:
        print("The quadrilateral is a rectangle.")
    else:
        print("The quadrilateral is a general quadrilateral.")
else:
    print("The angles do not form a valid quadrilateral.")


# In[ ]:


#Q29. Write a Python script to determine the season based on a user-provided month using elif statements.

month = int(input("Enter month number (1-12): "))

if month in [12, 1, 2]:
    print("It is winter.")
elif month in [3, 4, 5]:
    print("It is spring.")
elif month in [6, 7, 8]:
    print("It is summer.")
elif month in [9, 10, 11]:
    print("It is fall.")
else:
    print("Invalid month.")


# In[ ]:


#Q30. Implement a program to determine the type of a year (leap or common) and month (30 or 31 days) using elif statements.

year = int(input("Enter a year: "))
month = int(input("Enter month number (1-12): "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    leap_year = True
else:
    leap_year = False

if month in [1, 3, 5, 7, 8, 10, 12]:
    days = 31
elif month in [4, 6, 9, 11]:
    days = 30
elif month == 2:
    days = 29 if leap_year else 28
else:
    days = "Invalid month"

print(f"Month {month} has {days} days.")


# In[9]:


##Basic Level Questions:


# In[ ]:


#Q1. Write a Python program that checks if a given number is positive, negative, or zero.

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# In[ ]:


#Q2. Create a program to determine if a person is eligible to vote based on their age.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# In[ ]:


#Q3. Write a program to find the maximum of two given numbers using conditional statements.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("The maximum number is", num1)
else:
    print("The maximum number is", num2)


# In[ ]:


#Q4. Develop a program that calculates the grade of a student based on their exam score.

score = float(input("Enter the exam score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# In[ ]:


#Q5. Create a program that checks if a year is a leap year or not.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")


# In[ ]:


#Q6. Write a program to classify a triangle based on its sides' lengths.

side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")


# In[ ]:


#Q7. Build a program that determines the largest of three given numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is", num2)
else:
    print("The largest number is", num3)


# In[ ]:


#Q8. Develop a program that checks whether a character is a vowel or a consonant.

char = input("Enter a character: ").lower()

if char in 'aeiou':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")


# In[ ]:


#Q9. Create a program to calculate the total cost of a shopping cart based on discounts.

amount = float(input("Enter the purchase amount: "))

if amount >= 1000:
    discount = 0.2
elif amount >= 500:
    discount = 0.1
elif amount >= 100:
    discount = 0.05
else:
    discount = 0

total_cost = amount * (1 - discount)
print("The total cost after discount is", total_cost)


# In[ ]:


#Q10. Write a program that checks if a given number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


# In[10]:


##Intermediate Level Questions:


# In[ ]:


##Q11. Write a program that calculates the roots of a quadratic equation.

import cmath

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = cmath.sqrt(b**2 - 4*a*c)

root1 = (-b + discriminant) / (2*a)
root2 = (-b - discriminant) / (2*a)

print("The roots are", root1, "and", root2)


# In[ ]:


#Q12. Create a program that determines the day of the week based on the day number (1-7).

day = int(input("Enter a number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid number. Enter a number between 1 and 7.")


# In[ ]:


#Q13. Develop a program that calculates the factorial of a given number using recursion.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number: "))
print("The factorial is", factorial(number))


# In[ ]:


#Q14. Write a program to find the largest among three numbers without using the max() function.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2:
    if num1 >= num3:
        print("The largest number is", num1)
    else:
        print("The largest number is", num3)
else:
    if num2 >= num3:
        print("The largest number is", num2)
    else:
        print("The largest number is", num3)


# In[ ]:


#Q15. Create a program that simulates a basic ATM transaction menu.

balance = 1000

while True:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is", balance)
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful. New balance is", balance)
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful. New balance is", balance)
        else:
            print("Insufficient funds.")
    elif choice == 4:
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:


#Q16. Build a program that checks if a given string is a palindrome or not.

string = input("Enter a string: ").lower()
reversed_string = string[::-1]

if string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# In[ ]:


#Q17. Write a program that calculates the average of a list of numbers, excluding the smallest and largest values.

numbers = [float(x) for x in input("Enter numbers separated by space: ").split()]

if len(numbers) < 3:
    print("Not enough numbers to calculate average.")
else:
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    average = sum(numbers) / len(numbers)
    print("The average is", average)


# In[ ]:


#Q18. Develop a program that converts a given temperature from Celsius to Fahrenheit.

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("The temperature in Fahrenheit is", fahrenheit)


# In[ ]:


#Q19. Create a program that simulates a basic calculator for addition, subtraction, multiplication, and division.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Basic Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("The result is", add(num1, num2))
elif choice == '2':
    print("The result is", subtract(num1, num2))
elif choice == '3':
    print("The result is", multiply(num1, num2))
elif choice == '4':
    if num2 != 0:
        print("The result is", divide(num1, num2))
    else:
        print("Error: Division by zero.")
else:
    print("Invalid input.")


# In[ ]:


#Q20. Write a program that determines the roots of a cubic equation using the Cardano formula.

import math

def cubic_roots(a, b, c, d):
    delta0 = b**2 - 3*a*c
    delta1 = 2*b**3 - 9*a*b*c + 27*a**2*d
    C = ((delta1 + math.sqrt(delta1**2 - 4*delta0**3)) / 2)**(1/3)
    
    u = [1, (-1 + complex(0, math.sqrt(3)))/2, (-1 - complex(0, math.sqrt(3)))/2]
    
    roots = []
    for i in range(3):
        root = -1/(3*a) * (b + u[i]*C + delta0 / (u[i]*C))
        roots.append(root)
    
    return roots

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
d = float(input("Enter coefficient d: "))

roots = cubic_roots(a, b, c, d)
print("The roots of the cubic equation are:", roots)


# In[11]:


##Advanced Level Questions:


# In[ ]:


##Q21. Create a program that calculates the income tax based on the user's income and tax brackets.

income = float(input("Enter your income: "))

if income <= 10000:
    tax = 0
elif income <= 50000:
    tax = (income - 10000) * 0.1
elif income <= 100000:
    tax = (income - 50000) * 0.2 + 4000
else:
    tax = (income - 100000) * 0.3 + 15000

print("The tax owed is", tax)


# In[ ]:


#Q22. Write a program that simulates a rock-paper-scissors game against the computer.

import random

choices = ['rock', 'paper', 'scissors']
user_choice = input("Enter rock, paper, or scissors: ").lower()
computer_choice = random.choice(choices)

print("Computer chose", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == 'rock' and computer_choice == 'scissors') or      (user_choice == 'paper' and computer_choice == 'rock') or      (user_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")
else:
    print("You lose!")


# In[ ]:


#Q23. Develop a program that generates a random password based on user preferences (length, complexity).

import random
import string

length = int(input("Enter the length of the password: "))
complexity = input("Enter complexity level (low, medium, high): ").lower()

if complexity == 'low':
    characters = string.ascii_letters
elif complexity == 'medium':
    characters = string.ascii_letters + string.digits
elif complexity == 'high':
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid complexity level.")
    exit()

password = ''.join(random.choice(characters) for _ in range(length))
print("Your generated password is:", password)


# In[ ]:


#Q24. Create a program that implements a simple text-based adventure game with branching scenarios.

print("Welcome to the adventure game!")
print("You are in a dark forest. You see a path leading north and a cave entrance to the west.")
choice1 = input("Do you want to go north or enter the cave? ").lower()

if choice1 == 'north':
    print("You find a treasure chest filled with gold!")
elif choice1 == 'cave':
    print("You encounter a dragon! You need to find a way to escape.")
    choice2 = input("Do you want to fight the dragon or run away? ").lower()
    if choice2 == 'fight':
        print("You fight bravely and defeat the dragon!")
    elif choice2 == 'run':
        print("You escape safely and find your way back home.")
    else:
        print("Invalid choice. The dragon catches you.")
else:
    print("Invalid choice. You wander aimlessly and get lost.")


# In[ ]:


#Q25. Build a program that solves a linear equation for x, considering different cases.

def solve_linear(a, b):
    if a == 0:
        if b == 0:
            return "Infinite solutions."
        else:
            return "No solution."
    else:
        return -b / a

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))

solution = solve_linear(a, b)
print("The solution is", solution)


# In[ ]:


#Q26. Write a program that simulates a basic quiz game with multiple-choice questions and scoring.

questions = [
    {"question": "What is the capital of France?", "options": ["a. Berlin", "b. Madrid", "c. Paris"], "answer": "c"},
    {"question": "What is 2 + 2?", "options": ["a. 3", "b. 4", "c. 5"], "answer": "b"}
]

score = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer: ").lower()
    if answer == q["answer"]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")

print("Your final score is", score, "out of", len(questions))


# In[ ]:


#Q27. Develop a program that determines whether a given year is a prime number or not.

def is_prime(year):
    if year <= 1:
        return False
    for i in range(2, int(year**0.5) + 1):
        if year % i == 0:
            return False
    return True

year = int(input("Enter a year: "))

if is_prime(year):
    print("The year is a prime number.")
else:
    print("The year is not a prime number.")


# In[ ]:


#Q28. Create a program that sorts three numbers in ascending order using conditional statements.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 <= num2 <= num3:
    print(num1, num2, num3)
elif num1 <= num3 <= num2:
    print(num1, num3, num2)
elif num2 <= num1 <= num3:
    print(num2, num1, num3)
elif num2 <= num3 <= num1:
    print(num2, num3, num1)
elif num3 <= num1 <= num2:
    print(num3, num1, num2)
else:
    print(num3, num2, num1)


# In[ ]:


#Q29. Write a program that generates a random number within a given range and asks the user to guess it.

import random

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

number = random.randint(low, high)
guess = int(input(f"Guess the number between {low} and {high}: "))

if guess == number:
    print("Congratulations! You guessed it right.")
else:
    print(f"Sorry, the correct number was {number}.")


# In[ ]:


#Q30. Create a program that implements a simple contact management system with options to add, view, and delete contacts.

contacts = {}

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")
    elif choice == '2':
        if contacts:
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts available.")
    elif choice == '3':
        name = input("Enter the name of the contact to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == '4':
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Please try again.")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




