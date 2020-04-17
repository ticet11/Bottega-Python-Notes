# # Dictionary

car_dictionary = {
    "sensible": "Toyota Prius",
    "luxury": "Toyota Avalon",
    "muscle": "Ford Mustang",
    "clown": "VW Bus",
    "angry": "tank"
}

print(car_dictionary)

sensible_car = car_dictionary["sensible"]

print(sensible_car)

## will throw an error. Can not use a key that isn't defined or index.
# print(car_dictionary[butt])
# print(car_dictionary[0])

######################
# Nested Collections #
######################

teams = {
    "Sabres": ["Miller", "Roy", "Grier"],
    "Ducks" : ["Trout", "Puhols"],
    "Avalanche": ["Judge", "Stanton"]
}

print(teams["Sabres"])
print(teams["Ducks"])
print(teams["Avalanche"])

# setting a variable as a key/value pair, from the dictionary
sabres = teams["Sabres"]

print(sabres)

#######################
# Add Key/Value Pairs #
#######################

teams['Lightening'] = ["Price", 'Betts']

print(teams)

####################################
# Configure Fallback Lookup Values #
####################################

# .get() provides a fallback, to avoid errors, in case key does not exist.
featured_team = teams.get('mets', 'Not a thing, buddy.')

print(featured_team)

###########################
# Dictionary View Objects #
###########################

players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

# Makes working on the dictionary "Thread Safe" by creating a seperate instance of the dictionary
player_names = list(players.copy().values())
print(player_names)

# Key/ Value pairs can be returned as a "list", which can not be indexed.
# Dynamic, so if something changes in the dictionary, it will effect the view
print(players.values())

# Converts the value to a list, so it can be worked with in that manner.
print(list(players.values()))

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels" :  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items()

print(len(team_groupings))

# Retreaving nested information
print(list(team_groupings)[1][1][1])

##################################
# Deleting Items in a Dictionary #
##################################

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels" :  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

removed_team = teams.pop('yanks', "That's not even a team.")

print(teams)
print(removed_team)