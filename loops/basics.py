players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

# for single_item in collection
for player in players:
  print(player)

players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

# Allows access to players dictionary. 
# position - key1: player - key2
for position, player in players.items():
  print('Position', position)
  print('Player', player)

#########################
# Loop through a string #
#########################

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
  print(letter)

#######################
# Loop through ranges #
#######################

for num in range(1, 10):
  print(num)

for num in range(1, 10, 2):
  print(num)

######################
# Continue and Break #
######################

usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')

for username in usernames:
  if username == 'cersei':
    print(f'{username} was found at index {usernames.index(username)}')
    break
  print(username)

###############
# While Loops #
###############

# Must be told expicitly to stop looping.
nums = list(range(1, 100))

while len(nums) > 0:
  print(nums.pop())

def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == '42':
      print('Correct!')
      return False
    else:
      print(f'No go, buddy. {guess} is wrong. Try again.')

guessing_game()

#############################
# Combine and Flatten Lists #
#############################

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

for legacy_customer in legacy_customers:
  new_customers.append(legacy_customers)

print(new_customers)

######################
# List Comprehension #
######################

num_list = range(1, 11)
# cubed_nums = []

# The old way
# for num in num_list:
#     cubed_nums.append(num ** 3)

# The cute way.
# creates the new variable and builds the variable in one line.
cubed_nums = [num ** 3 for num in num_list]

print(list(num_list))
print(cubed_nums)

