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
