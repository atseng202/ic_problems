# Python implementation
    # split the words of the string but take into account
    # spaces, hyphens (and char must come before and after hyphen),
    # Also remove exclamation and periods from the words
    # Summary: 
    # 1. Split words when there is a space   
    # 2. Split words when there is a hyphen BUT make sure that there is a word before it
      # ... aka there was a legit character before the hyphen 
      # ... even if there is a space after a hyphen, we don't consider it a legit letter and
      # ... don't update the index at that space anyways
      # ... I take into account a space after a hyphen by only adding the word
      # ... when theres actual a word length > 0
    # 3. Periods and exclamations, we split the word before it
      # ... but also have to consider that there is a word to split 
      # ... so check that there is a suitable word length > 0
    # 4. apostrophes do nothing, consider it part of the word
class WordCloudData(object):

  def __init__(self, input_string):

     # Count the frequency of each word
     self.words_to_counts = {}
     self.populate_words_to_counts(input_string)

  def populate_words_to_counts(self, input_string):
    # using my helper method to split all the words into an array
    split_words = self.split_words(input_string)

    # Iterate in one pass, and consider all the cases for a word
    # Consider the two simple cases first
    # 1. is the word in the hash? 
    ## 1a. Is it capitalized and in the hash?
    ##  then we increment this capitalized version
    ## 1b. Is the word lowercase? 
    ## 1b. (cont.) check for uppercase version presence
    ## 1b. (cont.) and remove it from hash, adding that count to this lowercase version
    # 2. Otherwise, we have to consider:
    ## check if the word is capital or non-capitalized
    ## 2a. if un-capitalized, add the count in AND remove any capitalized version
    ## 2b. if this word is capitalized, check if the un-capitalized version
    ## 2b (cont.) is in the hash, and increment that lowercase accordingly
    ## 2b (cont.) and if not, this capitalized word is the ONLY version and add it in
    for word in split_words:
      capital_word = word.capitalize()
      if (self.words_to_counts.has_key(word)):
        # dict has the capitalized word already 
        # First case, is it capitalized?
        if (word[0].isupper()):
          self.words_to_counts[word] += 1
        else:
          # word is lowercased, i guess same as before
          self.words_to_counts[word] += 1
      else:
        # never seen word before
        # consider if uppercase or nah
        # case 1: is lowercase
        if word[0].islower():
          # now check for presence of any capitalized version
          # get the count, remove it, add it to our lowercase version
          if (self.words_to_counts.has_key(capital_word)):
            capital_count = self.words_to_counts[capital_word]
            self.words_to_counts.pop(capital_word)
            # add 1 for this current new lowercase word
            self.words_to_counts[word] = capital_count + 1
          else: 
            # no uppercase version of this word and this is first one
            self.words_to_counts[word] = 1
        else: 
          # new word is capitalized
          lowercase_word = word.lower()
          if (self.words_to_counts.has_key(lowercase_word)):
            # increment lowercase INSTEAD of upper
            self.words_to_counts[lowercase_word] += 1
          else:
            # this capitalized word is the first, there is no lowercase in here
            self.words_to_counts[word] = 1

    return self.words_to_counts


  
  # @staticmethod
  def split_words(self, input_string):
    words = []

    curr_word_length = 0
    curr_word_idx = 0
    input_length = len(input_string)

    # Plan: go thru the input string in one pass
    # Check if the char at current index is a letter with our helper method
    for idx, char in enumerate(input_string):
      if self.is_letter(char):
        # real letter, but we also need to update the index
        if curr_word_length == 0:
          curr_word_idx = idx
        
        # since it is a real letter, we increase length of the word 
        curr_word_length += 1

        # but we have to consider if this is the last index of the string
        if (idx == input_length - 1):
          word = "".join(input_string[curr_word_idx:curr_word_idx + curr_word_length])
          words.append(word)
          curr_word_length = 0
      elif curr_word_length > 0: 
        # not a character but could be any of the other stuff
        # like -, ?, !, " ", 
        # if its a " " everything before the space is taken 
        #UPDATE: i just make it so if its not a legit letter, I now check if the
        # word length is > 0 before doing anything else
        if (char == " "):
          word = "".join(input_string[curr_word_idx:curr_word_idx + curr_word_length])
          words.append(word)
          curr_word_length = 0
        elif (char == "-"):
          # see above for #2 case:
          # UPDATE: if there are letters before and after this char, it is still a part of the word
          if self.is_letter(input_string[idx - 1]) and self.is_letter(input_string[idx + 1]):
            curr_word_length += 1
          else:
            word = "".join(input_string[curr_word_idx:curr_word_idx + curr_word_length])
            words.append(word)
            curr_word_length = 0
        elif (char == "." or char == "!" or char == "?" or char == ":"):
          # consider end of sentences
          # periods are a special case, because they can be used like ...
          # But I do check for length of word in the upper block
          # after the first period, the next ones have no word length
          word = "".join(input_string[curr_word_idx:curr_word_idx + curr_word_length])
          words.append(word)
          curr_word_length = 0
    
    return words
      


  # @staticmethod
  def is_letter(self, character):
    return character in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\'"
    



# input = 'I like cake'
# input = 'Chocolate cake for dinner and pound cake for dessert'
# input = 'Strawberry short cake? Yum!'
# input = 'Dessert - mille-feuille cake'
# input = 'Mmm...mmm...decisions...decisions'
input = "Allie's Bakery: Sasha's Cakes"
data = WordCloudData(input)
# print(data.split_words(input))
# print(data.words_to_counts)