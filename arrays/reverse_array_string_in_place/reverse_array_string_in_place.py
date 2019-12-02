# Reverse a given list of characters in place
def reverse(string):
  first_idx = 0
  last_idx = len(string) - 1

  while first_idx < last_idx:
    latest_char = string[last_idx]
    string[last_idx] = string[first_idx]
    string[first_idx] = latest_char
    first_idx += 1
    last_idx -= 1

  
arr = ["l", "a", "t", "t", "e"]
reverse(arr)
print(arr)
  