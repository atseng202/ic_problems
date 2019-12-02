def merge_arrays(first, second):
  first_idx = 0
  second_idx = 0
  first_arr_length = len(first)
  second_arr_length = len(second)

  merged_array = []
  while (first_idx < first_arr_length and second_idx < second_arr_length):
    first_ele = first[first_idx]
    second_ele = second[second_idx]

    if first_ele <= second_ele:
      merged_array.append(first_ele)
      first_idx += 1
    else:
      merged_array.append(second_ele)
      second_idx += 1
  
  # Cleanup any array that hasnt been merged
  if (first_idx < first_arr_length):
    # first array needs to be completely merged
    while (first_idx < first_arr_length):
      ele = first[first_idx]
      merged_array.append(ele)
      first_idx += 1
  else: 
    while (second_idx < second_arr_length):
      ele = second[second_idx]
      merged_array.append(ele)
      second_idx += 1
  
  return merged_array



my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_arrays(my_list, alices_list))