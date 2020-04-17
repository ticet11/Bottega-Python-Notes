# Tuple is immutable
# List is mutable

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# This 'unpacking' would work for a list too.
# Because tuples are immutable, unpacking will be less prone to errors
title, sub_heading, content = post

print(title)
print(sub_heading)
print(content)

##############################
# Adding Elements to a Tuple #
##############################

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))

# The ',' is essential when combining tuples!
post += ('Wengus',)

print(id(post))

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)

##########################
# Lists Nested in Tuples #
##########################

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']

post += (tags,)

print(post[-1][1])

####################
# Slices in tuples #
####################

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

print(post[1::2])

###################
# Remove Elements #
###################

# post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# # Removing elements from end
# post = post[:-1]

# # Removing elements from beginning
# post = post[1:]

# # Removing specific element (messy/not recommended)
# post = list(post)
# post.remove('published')
# post = tuple(post)

# print(post)

###########################
# Tuple as Dictionary Key #
###########################

priority_index = {
  (1, 'premier'): [1, 34, 12],
  (1, 'mvp'): [84, 22, 24],
  (2, 'standard'): [93, 81, 3],
}

print(list(priority_index.keys()))

def top_items(priority_index):
    top_items_dic = {}
    for key, value in priority_index.items():
        if key[0] > 1:
            top_items_dic[key] = value
    return top_items_dic

print(top_items(priority_index))

##################################
# Guide to Python's Zip Function #
##################################

positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

# creates a new list of tuples from input lists
scoreboard = zip(positions, players)

print(list(scoreboard))