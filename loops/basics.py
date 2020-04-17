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