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

## Will remove first instance
users.remove('Brian')

print(users)

## .pop() removes last element in list and can return the popped element
popped_user = users.pop()

print(users)
print(popped_user)

del users[2]
print(users)

# # Dictionary
# car_dictionary = {
#     first_car: "Toyota Prius",
#     second_car: "Toyota Avalon",
#     future_car_one: "Ford Mustang",
#     future_car_two: "VW Bus"
# }

# # Tuple
