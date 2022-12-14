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

