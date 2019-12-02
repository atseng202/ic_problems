import random


def get_random(floor, ceiling):
  return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
  
  # Shuffle the input in place
  list_length = len(the_list)

  for index_we_are_randomizing in range(0, list_length):
    curr_value = the_list[index_we_are_randomizing]

    random_idx = get_random(index_we_are_randomizing, list_length - 1)
    if random_idx != index_we_are_randomizing:
      the_list[index_we_are_randomizing], the_list[random_idx] = the_list[random_idx], the_list[index_we_are_randomizing]
  

list = [1,2,3,4,5]
print(list)
shuffle(list)
print(list)

