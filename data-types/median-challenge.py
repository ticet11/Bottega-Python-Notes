#############################
# Find the Median challenge #
#############################

user_input = input("Give me a list of integers, seperated by spaces and I will return the median: ")
user_input = user_input.split()

sale_prices = []

for num in user_input:
    sale_prices.append(int(num))


def get_median():
    sale_prices.sort()
    sale_price_range_length = len(sale_prices)
    if sale_price_range_length % 2 == 0:
        median = (sale_prices[int(sale_price_range_length/2)] +
                  sale_prices[(int(sale_price_range_length/2)) - 1]) / 2
        print(f'{median} is the median')
    else:
        median = sale_prices[int(sale_price_range_length/2)]
        print(f'{median} is the median')

print("Wow, buddy, thanks. I'm gonna calculate this up and get that right out to you.")
get_median()
