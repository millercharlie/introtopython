# Welcome to Python!

# Python is a coding language developed in 1991 by Guido Van Rossum

# The language has an emphasis on readability and legibility

# Thus it is often used as a good language for newer coders to start out with

# Before we dive into the syntax and actually code in Python,
# It is important to define what coding is exactly and define 
# specific terms that are used in programming

# Code is a set of instructions that allows humans to dictate actions to computers.

# Programmers use code in many many ways

# Every single thing on the Internet was created using some sort of code

# This includes this very website, as well as every video game
# and application such as TikTok and YouTube

# In the real world, Python is used in data management and in 
# servers, among other things

# Now, it is time to begin coding

# Together, we will create a way to print text into this (-->)
# console here

# But first, let's get acquainted with data types

# But what are data types exactly?

# Data types are various forms of text that computers interpret differently

# For instance, any text, such as the phrase "Hello World!" 
# is a data type, called a String

# When the computer sees this specific data type, it knows 
# its a String and can handle it appropriately
# It's important to note that strings are represented with quotation marks
# Examples include ":)", "hi", "how are you?", "1", "True"

# Other forms of data types include ints, floats (also 
# sometimes called doubles), and booleans

# An int represents a whole number, which you may have learned about in school

# For instance, the numbers 0, 1, 2, 3, -1, -10, 124, and 
# everything of this sort are ints, or integers

# Floats represent any number with a decimal point
# Such as 1.0, 3.14, -2.9874921, 100.90

# Booleans represent True and False statements
# For instance, is it true that some apples are red?

# Alright, with that out of the way, we can begin our printing to the console

print('Hello World!')

# Let's break this down:

# in Python, syntax is relatively simple compared to other 
# languages, and only requires the word print()

# the word print represents printing to the console over here (-->)

# The parenthesis dictates what is to be printed

# Hence when you print "Hello World!" it appears on the Console as the 
# output of our program!

# It's important to note that in Python, code is executed line by line

# So if I were to write:

# print(":)")

# Both the first print statement and this print statement will run

# Pretty cool right?

# Now, I want you to practice by printing the phrase "Pets are cool!" into
# the console

... # TODO

# Now that that's out of the way, we can begin a new concept called 
# variables.

# Variables assign data to specific names

# Why is this important?

# Let's say we are creating a program to add two numbers together

# print(1 + 2)

# If we want to add one to the first number, we could have to constantly 
# rewrite this number

# print(2 + 2)
# print(3 + 2)
# print(4 + 2)
# print(5 + 2)

# Which could be a bit complicated

# Therefore, variables help us keep track of data

number = 1

# This is how variables are defined

# The word number is set to be the number 1

# Therefore, number includes a permanent referance to the number 1 unless 
# it is changed

# Let's visualize this:

# print(number)

# Here we can see that printing number actually prints 1, since we set number to equal 1

# I want you to practice variables by setting the word integer as 10

... # TODO

# Besides just numbers, the other data types we talked about earlier can 
# also be variables

phrase = "Hello World!"
cool = True
my_float = 10.0

# Now it is time to put our new knowledge of Python and data types to 
# good use

# Together, step by step, we will create a program to add the variable 
# number_one to the variable number_two and print the result

number_one = 1
number_two = 2
print(number_one + number_two)

# Practice: Ordering at a restaruant

# To begin with this project, we will first print out all the items on our restaurant's menu

# This restaurant will have 2 starters, 2 main course options, and 2 dessert options

print('salad')
print('breadsticks')
print('pizza')
print('pasta')
print('ice cream')
print('apple pie')

# Next, ask the user what they want to purchase for their appetizer.

# But wait, how do we 'ask' the user this?

# This is where the input() code comes in.

# This code captures the user input

# Let's look at an example

# name = input('What is your name? ')
# print('')
# print(name + ' is your name!')

# the input keyword tells the computer to capture everything the user writes

# The parenthesis is just a guiding phrase for the question

# Practice: write your own input to capture how the user is doing

# mood = input('How are you doing today? ')

# Anyways, we can put this to good use in our own program
# Go ahead and fill out the rest of this starter code below

# for the appetizer (starter)
starter = input('What appetizer would you like to order? ')

# for the main course
main = input('... ')

# for the dessert
dessert = ...

# Now, we will print out what the user ordered!

# for the starter
print("You ordered the " + starter + " as a starter!")

# for the main course
print("You ordered the " + ...)

# for the dessert
print(...)