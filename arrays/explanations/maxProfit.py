# Best Time to Buy and Sell Stock

def maxProfit(self, prices: List[int]) -> int:

# This line defines a function named `maxProfit`. The function takes two
# parameters: `self` and `prices`. `self` is typically used in the context of
# class methods, but here it seems unnecessary as the function isn't part of a
# class. `prices` is expected to be a list of integers. The function is expected
# to return an integer.

    max_profit = 0

# This line initializes a variable `max_profit` to 0. This variable will be used
# to keep track of the maximum profit that can be made from buying and selling a
# stock.

    min_price = float("inf")

# This line initializes a variable `min_price` to positive infinity. This
# variable will be used to keep track of the minimum price seen so far.

    for price in prices:

# This line starts a for loop that iterates over the `prices` list. For each
# iteration, the current price is stored in the `price` variable.

        if price < min_price:

# This line checks if the current price is less than the minimum price seen so
# far.

            min_price = price
        
# If the current price is less than the minimum price seen so far, this line
# updates `min_price` to the current price.

        elif price - min_price > max_profit:

# This line checks if the profit from selling at the current price (which is
# `price - min_price`) is greater than the maximum profit seen so far.

            max_profit = price - min_price

# If the profit from selling at the current price is greater than the maximum
# profit seen so far, this line updates `max_profit` to the current profit.

    return max_profit

# After the loop has finished, this line returns the maximum profit that can be
# made from buying and selling a stock. If no profit can be made, `max_profit`
# will remain 0 and the function will return 0.
