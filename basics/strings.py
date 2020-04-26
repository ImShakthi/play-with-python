#!/usr/bin/env python

data = "hello world"

print(data)

print(data[2:4])

# Try the exercises below
# 1. Make a program that displays your favourite actor/actress.
print("Tamanna")

# 2. Try to print the word ‘lucky’ inside s.
print("Whats digit %d in words? - seven" % 7)

# 3. Try to print the day, month, year in the form “Today is 2/2/2016”.
print("Today is %d/%d/%d" % (26, 4, 2020))


# Try the replace program
print(data.replace("world", "sakthivel"))

# Can a string be replaced twice?
# Does replace only work with words or also phrases?
text = "Hello world! Hello Earth"
print(text.replace("Hello", "hey", 1))

print(text.find("world"))

# Find out if string find is case sensitive
print(text.find("World"))

if "world" in text:
    print("we have world")

# What if a query string appers twice in the string?


# Write a program that asks console input and searches for a query.
data = input("Enter your name:")
print("Hello %s" % data)
