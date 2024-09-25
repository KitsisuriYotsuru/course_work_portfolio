# Python programming features - Week02-1
"""
a = b
b = c 

is "a" and "c" equal?
Yes: I can replace "b" with "a" in "b = c" to get "a = c"
"""

def function1(x):
    answer = x + 1
    return answer

def function2(x):
    return x + 1


# ---------------------------------------------------
# chaining
sentence = ' the cat is sleeping      '

# TODO: upper case words and strip leading/trailing spaces

print(sentence.upper().strip())

# ---------------------------------------------------
# single and double quotes

# TODO: Display the sentence: My cat's name is "Lucy"

print('My cat\'s name is "Lucy"')

# ---------------------------------------------------
# Formatted Strings

# TODO: display: I'm John and am 10 years old
name = 'John'
age = 10


# ---------------------------------------------------
# Lambda functions

def add_one(x):
    return x + 1

# Convert F to C
tempsF = [-40, 0, 32, 98.6, 212]

# TODO: Convert to Cel
values = []
for temp in tempsF:
    values.append(add_one(temp))
print(values)

values = []
for temp in tempsF:
    values.append((lambda t: t + 1)(temp))
print(values)

y = 10

# set x to 100 if y is less than 10 else set it to 1000

if y < 10:
    x = 100
else:
    x = 1000

x = 100 if y < 10 else 1000
