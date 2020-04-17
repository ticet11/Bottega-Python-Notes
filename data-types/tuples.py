# Tuple is immutable
# List is mutable

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# This 'unpacking' would work for a list too.
# Because tuples are immutable, unpacking will be less prone to errors
title, sub_heading, content = post

print(title)
print(sub_heading)
print(content)