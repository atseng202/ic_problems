# Write a function max_duffel_bag_value() 
# that takes a list of cake type tuples and a weight capacity, 
# and returns the maximum monetary value the duffel bag can hold.

def max_duffel_bag_value(cake_tuples, weight_capacity):
  table = [0] * (weight_capacity + 1)
  table[0] = 0

  for cake_tuple in cake_tuples:
    weight = cake_tuple[0]
    value = cake_tuple[1]

    # for bag_max_weight, bag_max_value in enumerate(table):
    for i in range(weight, len(table)):
      bag_max_weight = i
      bag_max_value = table[i]
      # take the current cake's value and consider the max_bag_weight - cake's current weight
      # the previous bag weight's max monetary value + current value will be compared with the current 
      # monetary value with the max value taken
      if weight == 0 and value > 0:
        # consider if any of the cake's have zero weight and value greater than 1, and return inf for that edge case
        return float('inf') 
      elif weight == 0:
        # a useless cake (weighs 0 and has value of zero)
        continue
      elif bag_max_weight - weight >= 0:
        # this is a legal weight in our table (>= 0)
        prev_max_value = table[bag_max_weight - weight]
        curr_potential_value = prev_max_value + value
        table[bag_max_weight] = max(curr_potential_value, bag_max_value)
        # if curr_potential_value > bag_max_value:
          # table[bag_max_weight] = curr_potential_value
      
    # print(table)
    
  return table[weight_capacity]



# Improve solution to keep track of maximum and avoid creating extra space
def max_duffel_bag_value_recursive(cake_tuples, weight_capacity, index = 0, memo = {}):
  key = (weight_capacity, index)
  if key in memo:
    return memo[key]
  if weight_capacity <= 0:
    return 0

  # cake_values = []
  current_max_value = None
  for idx in range(index, len(cake_tuples)):
    cake_tuple = cake_tuples[idx]
    weight = cake_tuple[0]
    value = cake_tuple[1]

    if weight == 0 and value > 0:
      memo[key] = float('inf')
      return float('inf')
    elif weight == 0:
      continue
    elif weight_capacity - weight >= 0: 
      current_sum = value + max_duffel_bag_value_recursive(cake_tuples, weight_capacity - weight, idx, memo)
      if current_max_value:
        current_max_value = max(current_max_value, current_sum)
      else:
        current_max_value = current_sum

      # cake_values.append(current_sum)
    else:
      continue

  if current_max_value:
    memo[key] = current_max_value
    return current_max_value
  else:
    memo[key] = 0
    return 0  


# print(max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7))
# print(max_duffel_bag_value_recursive([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7))


# print(max_duffel_bag_value([(4, 4), (5, 5)], 12))
# print(max_duffel_bag_value_recursive([(4, 4), (5, 5)], 12))


# print(max_duffel_bag_value([(2, 1)], 9))
print(max_duffel_bag_value_recursive([(2,1)], 9))
