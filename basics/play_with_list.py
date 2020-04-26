#!/usr/bin/env python

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',
          'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

print("\nAll US states")
for state in states:
    print(state)

print("\nStates with M")
for state in states:
    if 'M' in state or 'm' in state:
        print(state)


# Given the list y = [6,4,2] add the items 12, 8 and 4.
y = [6, 4, 2]
y.append(12)
y.append(8)
y.append(4)
print("items in y = ", y)

# Change the 2nd item of the list to 3.
y[1] = 3
print("items in y = ", y)


words = ["Be", "Car", "Always", "Door", "Eat"]
print(words)
words.sort()
print(words)
words = words[::-1]
print(words)


# Given a list with pairs, sort on the first element
x = [(3, 6), (4, 7), (5, 9), (8, 4), (3, 1)]
x.sort(key=lambda tup: tup[0])
print(x)

# Now sort on the second element
x = [(3, 6), (4, 7), (5, 9), (8, 4), (3, 1)]
x.sort(key=lambda tup: tup[1])
print(x)


# Create a list of one thousand numbers
thousand = list(range(1000))
# print(thousand)

# Get the largest and smallest number from that list
print("largest=", max(thousand))
print("smallest=", min(thousand))

# Create two lists, an even and odd one.
even = list(range(0, 10, 2))
print("even=", even)
odd = list(range(1, 10, 2))
print("odd=", odd)