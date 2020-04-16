#####################
# Lists: The Basics #
#####################

# Lists Example
car_list = ["Toyoto Prius", "Toyota Celica", "Ford Mustang", "VW Bug"]

print(car_list)

## inserts new item at index and moves all items, starting at index chosen and moves them down.
car_list.insert(1, "Ford Astro")

print(car_list)

## Add item to end of list
car_list.append('Chevy Cruze')

print(car_list)

## print a specific item. Allows use of specific methods for the object returned.
print(car_list[2])

## print the same item, but as it's own list
print([car_list[2]])

## reassign an index to a new value
car_list[4] = "Chevy Camero"
print(car_list)

###############################
# Remove Elements from a List #
###############################

users = ['Jan', 'Brian', 'Beth', 'Brian', 'Brian']

print(users)

## Will remove first instance (Have to know the value of the element to remove)
users.remove('Brian')

print(users)

## .pop() removes last element in list and can return the popped element
popped_user = users.pop()

print(users)
print(popped_user)

## simply deletes the chosen element from list (Have to know the index of the element to remove)
del users[2]
print(users)

########################################
# Nested Lists and Multiple Data Types #
########################################

users = ['Brian', 'Dand', 'Joel']

ids = [1,2,3]

# Mixed lists can be dangerous. If you try to do an operation that only works on ints on this list, like add,
# you will have an error
mixed_list = [42, 10.3, 'Altuve', users]

print(mixed_list)

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)

# Everything in this array is the same, because they are all arrays
nested_list = [[123], [234], [345], ['Brian']]

#########################################################
# Query Processes: len(), Negative Indexes, and index() #
#########################################################

tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags)
print(last_item)
print(index_of_last_item)

#################
# Sorting Lists #
#################

## Organizes in alphabetical order or numerical order

tags = ['python', 'development', 'tutorials', 'code']

print(tags)

tags.sort()

print(tags)

tags.sort(reverse=True)

print(tags)

totals = [234, 1, 543, 2345]

totals.sort(reverse=True)

print(totals)

###########################################
# Join Function to build URL Query String #
###########################################

# https://www.google.com/search?q=python+development+tutorial

uri = "https://www.google.com/search?q="
# tags = ['python', 'development', 'tutorial']

# # input requests an input from the user
# user_input = input("Name your pleasure!")
# tags = user_input.split()


# puts the string in between each of the elements
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'

print(query_uri)

####################
# Ranges in a List #
####################

tags = ['python', 'development', 'tutorials', 'code']

# pretty much the same as string ranges
tag_range = tags[1:2]
print(tag_range)

# This will grab everything from slice 1 to the end
tag_range = tags[1:]
print(tag_range)

# Grab everything from the beginning to slice 2.
tag_range = tags[:2]
print(tag_range)

# Grab all but the last element
tag_range = tags[:-1]
print(tag_range)

# Grab everything, for some reason
tag_range = tags[:]
print(tag_range)

tags = ['python', 'development', 'tutorials', 'code', 'programming', 'computer science']

# Grab every other element, starting with the first.
tag_range = tags[::2]
print(tag_range)

# Reverse the range.
## If you tried to use sort(reverse=True), you would end up with reverse alphabetical/numerical
tag_range = tags[::-1]
print(tag_range)

tag_range.sort(reverse=True)
print(tag_range)

## .sort() can not be stored (edits previous data, does not create anything new). 
# It returns a value of 'none'.
sorted_tags = tags.sort(reverse=True)
print(sorted_tags)

sale_prices = [
    100, 83, 220, 40, 100, 400, 10, 1, 3
]

## .sort() has changed the original content
# sale_prices.sort()
# print(sale_prices)

## .sorted() will return a new value without altering the previous content.
sorted_prices = sorted(sale_prices)
print(sorted_prices)
print(sale_prices)

# # Dictionary
# car_dictionary = {
#     first_car: "Toyota Prius",
#     second_car: "Toyota Avalon",
#     future_car_one: "Ford Mustang",
#     future_car_two: "VW Bus"
# }

# # Tuple
