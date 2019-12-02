def find_rotation_point(words):

    # Find the rotation point in the list
    # Use binary search to compare values
    # Get the middle index at each turn
    # If the word at middle_index is smaller than the word before and after it (return the index)
    # OR the array is size 2 and the word is smaller than the word before it (return the index)
    # OR the array is size 2 and the word is bigger than the word after it (return the index after)
    
    # If the word is bigger than the first word (we need to update the floor to be this index + 1)
    # If the word is smaller than the first word AND bigger than the word before AND smaller than word after
    ### (we've gone too far and the ceiling should be this index - 1)

    arr_length = len(words)
    floor_index = 0
    ceiling_index = len(words)

    while floor_index < ceiling_index:
        half_distance = (ceiling_index - floor_index) / 2
        middle_index = half_distance + floor_index
        middle_word = words[middle_index]
        # print(half_distance)

        index_before = middle_index - 1
        index_after = middle_index + 1

      # comparing only two values and half_distance is the right most value
        if index_before >= 0 and index_before < arr_length and half_distance == arr_length - 1 and middle_word < words[index_before]:
            return half_distance
        elif index_after >= 0 and index_after < arr_length and half_distance == 0 and middle_word > words[index_after]:
            return index_after
        elif index_before >= 0  and index_before < arr_length and index_after >= 0 and index_after < arr_length and middle_word < words[index_before] and middle_word < words[index_after]:
            return half_distance
      
      # Need to minimize size of array to half of previous size
        if middle_word > words[0]:
            floor_index = middle_index
        else:
            ceiling_index = middle_index

    return -1


arr = ['grape', 'orange', 'plum','radish', 'apple']
print(find_rotation_point(arr))