##############
# Data Types #
##############

# Booleans - True or false

# Numbers - Lot of different elements
int = 36
float = 36.0

# Strings - any type of byte sequence, from a word to a whole HTML doc
#   (can not be concatenated with a number)

# Bytes and byte arrays - pretty low level.

# None - ~Null, define variable w/o setting a real value.

#####################################
# More complex, low level variables #
#####################################

# Lists - ~Arrays
x = [2, 3, 4]
#

# Tuples - ~Arrays with parenthesis
x = (2, 3, 4)
# Good for deconstruction

# Sets -

# Dictionaries - Key value pairs
butt = 1
mud = 4
x = {butt: 2, mud: 3}

############
# Examples #
############

meal_completed = True
sub_total = 100
tip = sub_total * 1/5
total = sub_total + tip
receipt = "Your total is " + str(total)
print(receipt)
