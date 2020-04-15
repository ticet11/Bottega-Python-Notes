################
# Using quotes #
################

# Double quotes or single quotes are fine for a simple string.

sentence = "The quick brown fox jumps over the lazy dog."

print(sentence)

sentence = 'The quick brown fox jumps over the lazy dog.'

print(sentence)

# Without escaping, this sentence problem will have an error,
# because you have a single quote in the sentence.

sentence_problem = 'Tell my dog\'s mother, she is troubled.'

sentence_problem2 = "Tiffany said, \"That is my dog's mother!\""

print(sentence_problem)
print(sentence_problem2)

###############################
# Calling different processes #
###############################

# yes
sentence = "The quick brown fox jumps over the lazy dog.".upper()

print(sentence)

# no
sentence = "The quick brown fox jumps over the lazy dog."

# calling the process without assigning it to the variable
sentence.upper()

print(sentence)

# yes
sentence = "The quick brown fox jumps over the lazy dog."

print(sentence.upper())

# yes

sentence = "The quick brown fox jumps over the lazy dog."
sentence2 = sentence.upper()  # calls and then assins to variable 2

print(sentence)
print(sentence2)

#####################
# Changing the case #
#####################

# capitalizes first letter
sentence = "the quick brown fox jumps over the lazy dog".capitalize()
print(sentence)

# capitalizes all first letters
sentence = 'the quick brown fox jumps over the lazy dog'.title()
print(sentence)

# lowercase all letters
sentence = 'the QUICK brown fox juMps over the lazy dog'
print(sentence.lower())

#######################
# Portions of Strings #
#######################

# starter_sentence[0] = T
# starter_sentence[1] = h
starter_sentence = 'The quick brown fox jumps over the lazy dog'

# prints the first letter in the string
print(starter_sentence[0])

# Immutibility - You are not allowed to change the value of a string after it has been created
starter_sentence = 'The quick brown fox jumps over the lazy dog'
# starter_sentence[1] = 'p'

# This will pull an error
# print(starter_sentence)

# using the string data
first = starter_sentence[0]
second = starter_sentence[1]
third = starter_sentence[2]

new_sentence = first + second + third
print(new_sentence)

# Using ranges

starter_sentence = 'The quick brown fox jumps over the lazy dog'

# [start:stop:step]
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6  (slice position)
#    0   1   2   3   4   5    (index position)

first_word = starter_sentence[0:3]
print(first_word)

# creating a new sentence

starter_sentence = 'The quick brown fox jumped.'
new_sentence = 'Thy' + starter_sentence[3:27]
print(new_sentence)

# empty beginning or end of range = the edge
starter_sentence = 'The quick brown fox jumped.'
new_sentence = 'Thy' + starter_sentence[3:]
print(new_sentence)

# length function

new_sentence = 'Thy' + starter_sentence[3:len(starter_sentence)]
print(new_sentence)

# Flip the string!
starter_sentence = 'The quick brown fox jumped.'
print(starter_sentence[::-1])

############
# Heredocs #
############

# Multi-line strings

content = """
So far in this section about string's we've focused on strings
such as words and single line sentences. 
 
However, there are also times when you're going to have to work
with multi-line strings and that's what we're going to discuss
in this guide and multi-line strings in programming typically
are called `Heredocs` and just so you can see exactly how 
that's spelled and how you'd use it.
"""

print(content)

# .strip() removes empty spaces before and after string by default
# Can be used to remove whatever you pass through the function

stripped_content = """
So far in this section about string's we've focused on strings
such as words and single line sentences. 
 
However, there are also times when you're going to have to work
with multi-line strings and that's what we're going to discuss
in this guide and multi-line strings in programming typically
are called `Heredocs` and just so you can see exactly how 
that's spelled and how you'd use it.
""".strip()

print(stripped_content)

# repr() function gives you the low level version of your string

content = """
So far in this section about string's we've focused on strings
such as words and single line sentences. 
 
However, there are also times when you're going to have to work
with multi-line strings and that's what we're going to discuss
in this guide and multi-line strings in programming typically
are called `Heredocs` and just so you can see exactly how 
that's spelled and how you'd use it.
"""

print(repr(content))

# Can't use a heredoc? Use the repr() produced content on a single string.

long_string = "\nSo far in this section about string's we've focused on strings\nsuch as words and single line sentences. \n \nHowever, there are also times when you're going to have to work\nwith multi-line strings and that's what we're going to discuss\nin this guide and multi-line strings in programming typically\nare called `Heredocs` and just so you can see exactly how \nthat's spelled and how you'd use it.\n"

print(long_string)

#################
# Interpolation #
#################

name = 'Kristine'
# takes python code inside curly brackets, in this case an applicable variable.
# f prefix makes the line expect curly brackets
greeting = f'Hi, {name}'

print(greeting)

# Escaping {} to include
name = 'Kristine'
# Double brackets allow you to print the single set of brackets along with the string
greeting = f'{name} really likes these {{brackets}}'

print(greeting)

# Index based String Interpolation

name = 'Kristine'
age = 12
product = 'Python eLearning course'

# Ugly old way to know about

greeting = 'Product Purchase: {2} - Hi {0}, you are listed as {1} years old. - {3}'.format(
    name, age, product, 'Jordan')

print(greeting)

# Clean new way to be using.

from_name = 'Jordan'

greeting = f'Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_name}'

print(greeting)

#######################
# Finding a Substring #
#######################

sentence = 'The quick brown fox jumps over the lazy dog.'

query = sentence.find('quick')

# returns the index at which the substring starts.
print(query)

query = sentence.index('quick')

# returns the same index at which the substring starts
print(query)

query = sentence.find('oof')

# returns a -1 when not found.
print(query)

# query = sentence.index('oof')

# ## returns an error when not found
# print(query)

# returning boolean on whether substring is found in string.
query = 'fox' in sentence

print(query)

query = 'oof' in sentence

print(query)

##################################
# Find and Replace String Values #
##################################

sentence = 'The quick brown fox jumps over the quick dog.'

# Takes string to be replaced, followed by string to replace
# replaces all instances of the substring you've indicated
sentence = sentence.replace('quick', 'ugly')

print(sentence)

##################
# Negative Index #
##################

sentence = 'The quick brown fox jumps over the lazy dog.'

# [-1] would indicate the final character in the string
# [-2] = g
print(sentence[-1])

# range would still go front to back, so this will slice the last 4 characters and return.
print(sentence[-4:])

#########################
# strip, lstrip(), and rstrip() #
#########################

# strip the outside space
url = '    https://google.com       '
print(url.strip())

# strip a specific substring
url = 'https://google.com'
print(url.strip('https://'))

# utilizing lstrip, rstrip, and title to print 'Google'
url = 'https://google.com'
print(url.lstrip('https://').rstrip('.com').title())

######################
# Partition function #
######################

heading = 'Python: An Introduction'

# .partition() takes the breakpoint as the variable
# will only account for the first instance of the variable in the string
header, _, subheader = heading.partition(': ')

print(header)

print(subheader)

heading = f'{header} {subheader}'
print(heading)

# storing the partition output into a variable
heading = 'Python: An Introduction'
x = heading.partition(': ')

# prints a tuple with 3 elements
print(x)

##################
# split function #
##################

tags_string = 'python,coding,programming,development'

# Splits at the variable passed through, the comma in this example.
tags_list = tags_string.split(',')

print(tags_list)

# No variable passed through simply converts 
# your string into a list with the string as the only element.
tags_list = tags_string.split()

print(tags_list)

#################################################################
# Check if string represents numbers or alphanumeric characters #
#################################################################

api_data = '5'
greeting = 'Hello'

print(api_data.isalpha()) # returns False, string is a number
print(greeting.isalpha()) # returns true, string is alphanumeric

print(api_data.isnumeric()) # returns True, the string is a number
print(greeting.isnumeric()) # returns False, string is alphanumeric