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