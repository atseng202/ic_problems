def find_repeat(numbers):
  # Since we must make sure space complexity is not abused, at best we can sort the array
  # and then find repeats that way with O(nlgn) complexity
  # but that destroys the input's order so a better way is to 
  # use binary search to search sub-ranges of 1 to n given that
  # the question says we have values distinct from 1 to n and a total
  # of n + 1 items
  # meaning there has to be a duplicate 
  # so binary search in half ranges, checking n items in the array for 
  # counts that belong in each range and if there are more counts for that range
  # than there are legal distinct numbers possible like 1...3
  # i.e. the count is 6 (n + 1) but the range is 1 to 5 and 6 > 5 
  floor = 1
  ceiling = len(numbers) - 1

  while floor < ceiling:
    midpoint = floor + (ceiling - floor) / 2
    lower_floor = floor 
    lower_ceiling = midpoint
    higher_floor = midpoint + 1
    higher_ceiling = ceiling

    # in original range it should be n distinct items
    # take the ceiling - floor + 1
    distinct_number_of_items_in_lower_range = lower_ceiling - lower_floor + 1

    number_of_items_in_lower_range = 0
    for number in numbers:
      if number >= lower_floor and number <= lower_ceiling:
        number_of_items_in_lower_range += 1
    
    if number_of_items_in_lower_range > distinct_number_of_items_in_lower_range:
      # this is the range we focus on
      floor = lower_floor
      ceiling = lower_ceiling 
    else:
      floor = higher_floor
      ceiling = higher_ceiling
  
  return floor
