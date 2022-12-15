#Variables
## Python lets us store information in variables
price = 10 #integer
rating = 4.9 #float
name = 'Mosh' #string
is_published = False #Boolean 
print(price)

#exercises

full_name = 'John Smith'
age = 20
is_new = True

#Receiving Input

name = input('What is your name? ')
print('Hi ' + name)

#exercises

color = input('What is your favorite color?')
print(name + ' likes ' + color)

# Type Conversion
# How to convert a string to an integer to vice versa

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)
print (type(age))

#exercise

weight_lbs = input('weight (lbs)')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

#strings

course = "Python's Course for Beginners" # use double quotes if you need inside single quotes
course = 'Python for "Beginners"' # or vice verse
course = '''
Hi John 
Go do some work
'''
###########

course = 'Python for Beginners'

print(course[-2]) #will print the second to last char from left

print(course[0:3])

# Formatted Strings- use curly braces

first = 'John'
last = "Smith"
message = first + ' [' + last + '] is a coder' #concatenated solution
msg = f'{first} [{last}] is a coder' # formatted string
print(message)
print(msg)

# String Methods

course = 'Python for Beginners'
print(len(course)) #length function- it can count the number of items
# len and print are general purpose functions and dont belong to anyone
# methods belong to strings
print (course.upper())
print (course.lower())
print(course.find('P'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners')) #remember this is case-sensitive

print('Python' in course) # will produce a Boolean value // The "in" operator

# when a function belongs to something we refer to it as a method


# Arithmetic Operations

print (10 // 3) #will divide with an integer
print (10 ** 3) #exponent

x = 10
x = x + 3
print(x)

x += 3

print(x)

x -= 6
print(x)

# Operator Precedence

x = 10 + 3 * 2 #order of operations
print(x)

# Math functions

x= 2.9
print(round(x))
print(abs(-2.9))

import math


math.ceil(2.9)


# If Statements

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink Plenty of water")
elif is_cold: 
    print("It's a cold day")
    print("Wear Warm Clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

price_house = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price_house
else:
    down_payment = 0.2 * price_house
print(f"DownPayment: ${down_payment}")

# logical operators

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("eligible for loan")

if has_high_income or has_good_credit:
    print("eligible for loan")

# AND : both
# OR : at least one
# NOT

# Comparison Operators

temperature = 30 

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

name = "J"

if len(name) < 3:
    print("Name must be at least 3 chars!")
elif len(name) > 50:
    print("Name is max of 50 chars")
else:
    print("Name looks good")

    # Weight converter project

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")
elif unit.upper() == "K":
    converted = weight / 0.45
    print(f"You are {converted} pounds")




    # While Loop

i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Done")


# While Loop

i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")


# Guessing Game

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
   guess = int(input('Guess: '))
   guess_count += 1
   if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you failed.')

# Car Game
command = ""
started = False
while True:
   command = input("> ").lower()
   if command == "start":
      if started:
            print("Car is already started")
      else:
         started = True
         print("Car started ...")
   elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
         started = False
         print("Car stopped.")
   elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
    """)
   elif command == "quit":
        break
   else:
    print("Sorry I don't understand that!")

    

# For Loops

prices = [10, 20, 30]

total = 0
for price in prices:
    total += price # audgemented assignment opp
print(f"Total: {total}")

# Nested Loops

for x in range(4):
    for y in range(3):
        print(f'({x} - {y})')

# More Nested Loops

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range (x_count):
        output += 'x'
    print(output)

# Lists

names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Jon'
print(names[2:])
print(names)

# Largest Number in List

numbers = [12, 3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

# 2D Lists- x and y

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

print(matrix[0][1])

# Remove Duplicates

numbers = [2, 2, 4, 5, 3, 4, 6, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

# Tuples- Go for when you don't want to modify a list

numbers = (1, 2, 3)
numbers[0] = 10
print(numbers[0])

