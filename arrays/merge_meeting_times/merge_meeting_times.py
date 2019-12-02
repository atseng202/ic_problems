# Key function for sorting the meeting
def sort_by_time(obj):
  return obj[0]

def merge_ranges(ranges_arr):
  sorted_ranges_arr = sorted(ranges_arr, key=sort_by_time)
  # After sorting the ranges, O(nlgn), now iterate thru the arr
  # and check for any ranges that should output into final array
  final_ranges = [sorted_ranges_arr[0]]
  range_length = len(sorted_ranges_arr)
  
  # print(sorted_ranges_arr)
  for idx, range_tuple in enumerate(sorted_ranges_arr, start=1):
    # starting from idx 1 because we will be comparing with the 
    # latest range in the final_ranges array
    current_start = range_tuple[0]
    current_end = range_tuple[1]
    prev_end = final_ranges[-1][1]
    prev_start = final_ranges[-1][0]

    if current_start <= prev_end:
      # current start time is in the range of the previous range
      # update the prev_end to be the max of the current_end and prev_end
      final_ranges[-1] = (prev_start, max(current_end, prev_end))
    else: 
      # current start time is out of the range of the previous range
      # add it into the array
      final_ranges.append((current_start, current_end))
    

  
  return final_ranges

print(merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]))
