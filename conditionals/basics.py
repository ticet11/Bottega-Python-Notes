# Single condition
age = 25

if age < 25:
  print(f"I'm sorry, you need to be at least 25 years old")

# if/else
age = 55

if age < 25:
  print(f"I'm sorry, {age} is under 25 years old")
else:
  print(f"You're good to go, {age} fits in the range to rent a car")

# if/elif/else
age = 55

if age < 25:
  print(f"I'm sorry, {age} is under 25 years old")
elif age > 100:
  print(f"I'm sorry, {age} is over 100 years old")
else:
  print(f"You're good to go, {age} fits in the range to rent a car")

####################
# Ternary Operator #
####################

role = 'admin'

# Old way
if role == 'admin':
    auth = 'can access'
else:
    auth = 'can not access'

print(f'This user {auth}.')

# cute way
auth = 'can access' if role == 'admin' else 'cannot access'

print(f'This user {auth}.')

#########################
# Conditional Operators #
#########################

# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

username = 'jonsnow'

if username == 'jonsnow':
  print('Welcome Jon')
else:
  print('You shall not pass!')

age = 25

if age <= 25:
  print(f"I'm sorry, you need to be at least 25 years old")

# Comparing lists
users = ['Kris', 'Jan']
users_2 = ['Kris', 'Jan']

if users == users_2:
    print('Wow, same.')

#########################################
# Check for value inside string or list #
#########################################

sentence = 'The quick brown fox jumps over the lazy Dog'
word = 'dog'

if word.lower() in sentence.lower():
  print('The word is in the sentence')
else:
  print('The word is not in the sentence')


nums = [1, 2, 3, 4]

if 3 in nums:
  print('The number was found')
else:
  print('The number was not found')