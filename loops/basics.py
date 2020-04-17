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