def get_permutations(string):
  # what is the base case?
  # append anything in the set
  # this method returns a set so the base case must return a set 
  # base case of empty, return empty set
  # base case of 1 letter, return set with 1 letter
  
  if len(string) == 1:
    return set(string)
  if len(string) == 0:
    return set([''])
  
  # n case, there are more than 1 letters in the string, like 2
  # if n = 2, we take the permutation of n - 1 letters, and iterate thru that 
  # if n = 3, we take the permutation of 2 letters, and iterate thru that
  # so for 'ab', string before is 'a' and recursed permutation will return set('a')
  string_before_last_letter = string[0:len(string) - 1]
  recursed_permutations_set = get_permutations(string_before_last_letter)
  last_letter = string[-1]

  # use a loop to properly add our current letter to every permutation for each word in the set
  new_set = set()
  for word in recursed_permutations_set:
    # will need to remove this word from the set after
    for idx in range(0, len(word) + 1):
      new_word = word[0:idx] + last_letter + word[idx:len(word)]
      new_set.add(new_word)
    
  
  return new_set
  
def get_permutations_iterative(string):
  perms = []

  for letter in string:
    if len(perms):
      current_words_length = len(perms)
      while current_words_length > 0:

        word = perms.pop(0)

        for idx in range(0, len(word) + 1):
          new_word = word[0:idx] + letter + word[idx:len(word)]
          perms.append(new_word)

        current_words_length -= 1
    else:
      perms.append(letter)
  
  return perms

word = ''
print(get_permutations(word))