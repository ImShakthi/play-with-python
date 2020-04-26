#!/usr/bin/env python

words = {}
words["BMP"] = "Bitmap"
words["BTW"] = "By The Way"
words["BRB"] = "Be Right Back"

print(words["BMP"])
print(words["BRB"])


# Make a mapping from countries to country short codes
# Print each item (key and value)
countries = {"IN": "India", "PAK": "Pakistan", "SL": "Srilanka"}
for code, name in countries.items():
    print(code, name)

baskets = {"apple", "orange", "apple"}
print("basket is full of ", baskets)

# list
questions = ["first", "second", "third"]
answers = ["sunday", "monday", "tuesday"]
for q, a in zip(questions, answers):
    print("what is the {0} day of a week? Answer: {1}".format(q, a))
