memo = {}
def change_possibilities(amount, denominations, current_index=0):

  # Calculate the number of ways to make change
  # Base case, we reduced the amount to either 0 or less than 0
  # But if there are no coins, then there is no way to get any amount in the first place
  # Also bad to break apart of denominations, so I should keep track of index
  memo_key = str((amount, current_index))
  if memo_key in memo:
    print "Retrieving from memo: %s" % memo_key
    return memo[memo_key]

  # if len(denominations) == 0:
    # return 0
  if amount < 0:
    return 0
  if amount == 0:
    return 1

  print "checking ways to make %i with %s" % (
    amount,
    denominations[current_index:]
  )

  # n case, we loop through the coins and recurse
  # O(n * m) time where n is amount, and m is the number of denominations
  # O(n * m) space since for every m and value from n to 0, we call the function
  total_possibilities = 0
  # I wanted to iterate starting from current_index
  
  for idx in range(current_index, len(denominations)):
    coin_val = denominations[idx]
    # consider each coin_val
    # reducing the amount by the coin_val each time
    # if amount reaches 0, we will get another possibility
    reduced_amount = amount - coin_val
    if reduced_amount < 0:
      break

    print "Amount left is %i and current idx is %i" % (amount, idx)
    potential_possibilities = change_possibilities(reduced_amount, denominations, idx)
    total_possibilities += potential_possibilities
  
  # print(total_possibilities)
  memo[memo_key] = total_possibilities
  return total_possibilities


# Time complexity: O(N * M) N being amount, M is # of denominations
# Space complexity: O(N), ways to make from 0 to N amounts
def change_iterative(amount, denominations):
  # Try to compute for smaller amounts first up until we get to the largest amount
  if len(denominations) == 0:
    return 0
  if amount == 0:
    return 1

  # compute the answer for a smaller amount starting at 1
  # use this answer to iteratively compute for higher values until arriving at a final 'amount'
  # to account for 0 cents, I add amount + 1
  ways_to_make_n_cents = [0] * (amount + 1)
  ways_to_make_n_cents[0] = 1
  for coin in denominations:
    # using each coin, find how many ways to make n cents with that coin and add it into our list where 
    # the index is the number of cents, and value is the number of ways to make that amount i.e. (0 cents, 1 way), (1 cent, 1 way), (2 cents, 1 way) if we have 1 cent
    for number_of_cents in range(coin, amount + 1):
    # for number_of_cents in range(1, len(ways_to_make_n_cents)):
      # find out if its possible to use the coin to make this number of cents
      # if number_of_cents - coin < 0:
        # continue
      # new ways to make n cents includes the previous number of possibilities  + the possibilities we have built up without using this coin
      ways_to_make_n_cents[number_of_cents] = ways_to_make_n_cents[number_of_cents] + ways_to_make_n_cents[number_of_cents - coin]

  return ways_to_make_n_cents[amount]




# i.e. amount=4, denom=[1,2,3]
# 1-1-1-1, 1-1-2, 1-3, 2-2
# i see a tree here of options, and I recurse up after every successful option to return an increment of 1
# actual = change_possibilities(4, (1, 2, 3))

# print(actual)
print(change_iterative(4, (1,2,3)))
