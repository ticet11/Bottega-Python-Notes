################
# Number Types #
################

# int
product_id = 123

# float - less granular than a decimal
sale_price = 14.95

# fraction
tip_percentage = 1/5

## Different number types can be combined.
    # Will dynamically convert data types when necessary.

##########################
# Mathematical Operators #
##########################

print('Addition')
print(100 + 42)

print('Subtraction')
print(100 - 42)

print('Division')
print(100 / 42)
print(100 / 38)

print('Floor Division')
print(100 // 42)
print(100 // 38)

print('Multiplication')
print(100 * 42)

print('Modulus')
print(100 % 42)

print('Exponents')
print(100 ** 42)

#######################
# Order of Operations #
#######################

"""
P - ()
E - **x
(M - * -> D - /)
(A - + -> S - -)
"""

calculation = 8 + 2 * 5 - (9 + 2) ** 2
print(calculation)

########################
# Assignment Operators #
########################

total = 100

# same as 'total = total + 10'
total += 10

## will work similarly with -=, *=, /=, //=, **=, %=

print(total)

####################
# Decimal vs Float #
####################

# program from company trying to add cost of sales
#  person's commission to each product sold to show total cost
# to company
product_cost = 88.40
commission_rate = 0.08
quantity = 450

product_cost += (commission_rate * product_cost)
print(product_cost * quantity) # 42962.4

# # Utilizing a decimal instead of a float 
# # (Decimal provides higher precision)
# from decimal import Decimal

# product_cost = Decimal(88.4)
# commission_rate = Decimal(.08)
# quantity = 450

# product_cost += (commission_rate * product_cost)
# print(product_cost * quantity) # 42962.40000000000282883716451

################################################
# Converting between sub-data-types in numbers #
################################################

product_cost = 88.40
commission_rate = 0.08
quantity = 450

# removes whatever comes after the decimal, does not round up
print(int(product_cost))

# adds .0 on the end
print(float(quantity))

# displays the full decimal version of the number
# print(Decimal(product_cost))

# gives scientific notation
print(complex(commission_rate))

##########################
# Popular Math Functions #
##########################

import math

loss = -20.25
product_cost = 89.99

# absolute value (math not required)
print(abs(loss))

# removes decimal after whole number
print(math.floor(product_cost))

# ceiling - rounds up to nearest whole number
print(math.ceil(product_cost))

print(loss)
## goes to -21, because -21 is lower than -20
print(math.floor(loss))

## the most inner parenthesis are used first and then moves outward.
print(abs(math.floor(loss)))

# square root
print(math.sqrt(product_cost))

# exponential power - more specific and complex 
# than regular exponent
print(math.pow(5, 2))
