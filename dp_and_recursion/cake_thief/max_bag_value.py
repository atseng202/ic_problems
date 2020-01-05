# Write a function max_duffel_bag_value() 
# that takes a list of cake type tuples and a weight capacity, 
# and returns the maximum monetary value the duffel bag can hold.
import unittest

# Improve solution to keep track of maximum and avoid creating extra space
def max_duffel_bag_value(cake_tuples, weight_capacity, index = 0, memo = {}):
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
      current_sum = value + max_duffel_bag_value(cake_tuples, weight_capacity - weight, idx, memo)
      if current_max_value:
        current_max_value = max(current_max_value, current_sum)
      else:
        current_max_value = current_sum

      cake_values.append(current_sum)
    else:
      continue

  if current_max_value:
    memo[key] = current_max_value
    return current_max_value
  else:
    memo[key] = 0
    return 0  

class Test(unittest.TestCase):
  def setUp(self):
    self.memo = {}
  
  def tearDown(self):
    self.memo = {}

  def test_one_cake(self):
    actual = max_duffel_bag_value([(2, 1)], 9, 0, self.memo)
    expected = 4    
    self.assertEqual(actual, expected)

  def test_two_cakes(self):
    actual = max_duffel_bag_value([(4, 4), (5, 5)], 9, 0, self.memo)
    expected = 9
    self.assertEqual(actual, expected)

  def test_only_take_less_valuable_cake(self):
    actual = max_duffel_bag_value([(4, 4), (5, 5)], 12, 0, self.memo)
    expected = 12
    self.assertEqual(actual, expected)

  def test_lots_of_cakes(self):
    actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7, 0, self.memo)
    expected = 12
    self.assertEqual(actual, expected)

  def test_value_to_weight_ratio_is_not_optimal(self):
    actual = max_duffel_bag_value([(51, 52), (50, 50)], 100, 0, self.memo)
    expected = 100
    self.assertEqual(actual, expected)

  def test_zero_capacity(self):
    actual = max_duffel_bag_value([(1, 2)], 0, 0, self.memo)
    expected = 0
    self.assertEqual(actual, expected)

  def test_cake_with_zero_value_and_weight(self):
    actual = max_duffel_bag_value([(0, 0), (2, 1)], 7, 0, self.memo)
    expected = 3
    self.assertEqual(actual, expected)

  def test_cake_with_non_zero_value_and_zero_weight(self):
    actual = max_duffel_bag_value([(0, 5)], 5, 0, self.memo)
    expected = float('inf')
    self.assertEqual(actual, expected)


unittest.main(verbosity=2)
