# Python Implementation
# will use a set instead as practice

def has_palindrome_permutation(string):
  unpaired_chars = set()

  for char in string:
    if char in unpaired_chars:
      # Previously odd, now even so remove 
      unpaired_chars.remove(char)
    else:
      # Unseen, so either never seen or even before, so we add
      unpaired_chars.add(char)
  
  return len(unpaired_chars) <= 1
