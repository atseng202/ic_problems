# Greedy approach: Keep track of the max profit at each point
# we can do so by keeping track of the current minimum at each pass
def get_max_profit(stock_prices):
  if len(stock_prices) < 2:
    raise ValueError("Cannot have stock count less than 2")
  
  min_price = stock_prices[0]
  max_profit = None

  # for idx, curr_price in enumerate(stock_prices, start=2):
  for idx in range(1, len(stock_prices)):
    curr_price = stock_prices[idx]
    curr_profit = curr_price - min_price 
    
    if max_profit == None:
      max_profit = curr_profit
    else:
      max_profit = max(curr_profit, max_profit)

    min_price = min(curr_price, min_price)

  return max_profit



prices = [9, 7, 4, 1]
print(get_max_profit(prices))