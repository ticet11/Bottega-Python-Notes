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
