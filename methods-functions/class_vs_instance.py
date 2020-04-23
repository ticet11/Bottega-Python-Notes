"""
class Website:
    def __init__(self, title):
        self.title = title

ws = Website('My Website Title')

# Will print a dictionary of the variables and their values
print(ws.__dict__)

ws_two = Website('Second Title')
print(ws_two.__dict__)
"""

class DifferentWebsite:
    title = 'My Class Title'


dws = DifferentWebsite()
# Doesn't print anything, because it only applies to instance attributes,
# Something passed through the class.
print(dws.__dict__)

# A class attribute belongs to the class definition

# An instance attribute belongs only to the instance it was paired with