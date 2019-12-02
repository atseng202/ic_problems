# Take array of characters with space separating each word
# reverses array in place

# Brute force: Reverse all characters in the array
# Then reverse each word individually for a time complexity of n + n^2

# Helper
def reverse(string, left_idx, right_idx):
  first_idx = 0

  while left_idx < right_idx:
    latest_char = string[right_idx]
    string[right_idx] = string[left_idx]
    string[left_idx] = latest_char
    left_idx += 1
    right_idx -= 1

# O(n) for first reversal, then iterate thru the message and reverse each word when we reach a space

def reverse_words(message):
  reverse(message, 0, len(message) - 1)

  curr_left_idx = 0
  curr_right_idx = None

  for i, word in enumerate(message):
    if word == " " or i == len(message) - 1:
      if word == " ":
        curr_right_idx = i - 1
      else:
        curr_right_idx = i

      reverse(message, curr_left_idx, curr_right_idx)
      # while curr_left_idx < curr_right_idx:
      #   message[curr_left_idx], message[curr_right_idx] = message[curr_right_idx], message[curr_left_idx]
      #   curr_left_idx += 1
      #   curr_right_idx -= 1

      # Reset left_idx
      curr_left_idx = i + 1
      


message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

print(''.join(message))

## Optimal Solution
# We reverse the string in place once
# O(n)
# Then iterate one more time, and reverse as needed 
# if we go thru the whole word and only have to reverse once then thats just 1 pass of swapping
# so it's still O(n)
# in other words, I reverse an n word list once, or a bunch of words n - x times for a total of n 
