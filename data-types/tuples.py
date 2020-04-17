# Tuple is immutable
# List is mutable

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# This 'unpacking' would work for a list too.
# Because tuples are immutable, unpacking will be less prone to errors
title, sub_heading, content = post

print(title)
print(sub_heading)
print(content)

print(id(title))
##############################
# Adding Elements to a Tuple #
##############################

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))

# The ',' is essential when combining tuples!
post += ('Wengus',)

print(id(post))



title, sub_heading, content, status = post

print(id(title))

print(title)
print(sub_heading)
print(content)
print(status)