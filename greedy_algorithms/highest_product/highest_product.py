def highest_product_of_3(list_of_ints):
  if len(list_of_ints) < 3:
    raise ValueError("must have at least 3 integers")

  highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
  highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
  lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]
  highest = list_of_ints[0] if list_of_ints[0] > list_of_ints[1] else list_of_ints[1]
  lowest = list_of_ints[0] if list_of_ints[0] < list_of_ints[1] else list_of_ints[1]

  for i in range(2, len(list_of_ints)):
    current = list_of_ints[i]
    # Update the highest_product_of_3
    if (highest_product_of_2 * current > highest_product_of_3):
      highest_product_of_3 = highest_product_of_2 * current
    if (lowest_product_of_2 * current > highest_product_of_3):
      highest_product_of_3 = lowest_product_of_2 * current 

    # Update highest_product_of_2 and lowest of 2
    if (highest * current > highest_product_of_2):
      highest_product_of_2 = highest * current
    if lowest * current > highest_product_of_2:
      highest_product_of_2 = lowest * current

    if highest * current < lowest_product_of_2:
      lowest_product_of_2 = highest * current
    if lowest * current < lowest_product_of_2:
      lowest_product_of_2 = lowest * current

    # Finally, update the highest and lowest at this current number
    if current > highest:
      highest = current 
    if current < lowest:
      lowest = current
  
  return highest_product_of_3