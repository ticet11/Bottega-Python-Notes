################
# Basic Syntax #
################

def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')

def auth(email, password):
  if email == 'kristine@hudgens.com' and password == 'secret':
    print('You are authorized')
  else:
    print('You are not authorized')


auth('kristine@hudgens.com', 'asdf')

def hundred():
  for num in range(1, 101):
    print(num)


hundred()

def counter(max_value):
  for num in range(1, max_value):
    print(num)


counter(501)

#####################
# Returning a value #
#####################

# return creates usable data. 
# Your complex programs will not use the terminal as an interface,
# so you will not need the final product to print to the terminal.
# You will need to create data, accessible by the UI.
def full_name(first, last):
  return f'{first} {last}'


kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
  print(f'Hi {name}!')


greeting(kristine)

#####################
# Nesting functions #
#####################

def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')