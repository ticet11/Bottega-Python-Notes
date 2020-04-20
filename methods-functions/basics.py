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

#####################
# Default Arguments #
#####################

def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Nope
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())

############################
# Named function arguments #
############################

def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')
full_name(first = 'Kristine', last = 'Hudgens')
full_name(last = 'Hudgens', first = 'Kristine')

######################
# Argument Unpacking #
######################

# Allows you to take multiple arguments in at a time,
# without stating them in the function.
# creates a tuple.  
def greeting(*args):
  print('Hi ' + ' '.join(args))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')

# args is best practice, but not required
def greeting(*names):
  print('Hi ' + ' '.join(names))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')

# combining argument types.
def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')

#####################
# Keyword Arguments #
#####################

def greeting(**kwargs):
    if kwargs:
        print(f"Hi, {kwargs['first_name']} {kwargs['last_name']}, what it do?")
    else:
        print('Hello, stranger. You are not welcome.')

greeting(first_name = 'Jengus', last_name = 'Khan')
greeting()

##########################
# Combine Argument Types #
##########################

def greeting(time_of_day, *args, **kwargs):
    print(f"Hi, {' '.join(args)}, I hope you will bee cool this {time_of_day}")

    if kwargs:
        print('Your tasks for the day are:')
        for key, value in kwargs.items():
            print(f"{key} => {value}")

greeting('morning', 
         'Brian', 'Michael', 'Kozub',
          first = 'Wash Dishes',
          second = 'Be good',
          third = 'Start again')