def sort_scores(unsorted_scores, highest_possible_score):
  scores_hash = {}

  for score in unsorted_scores:
    if score in scores_hash:
      scores_hash[score] += 1
    else:
      scores_hash[score] = 1
  
  # Hash made, now create our array
  sorted_scores = []
  for number in range(100, -1, -1):
    if number in scores_hash:
      freq = scores_hash[number]
      for i in range(freq):
        sorted_scores.append(number)
    
  
  return sorted_scores


unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))