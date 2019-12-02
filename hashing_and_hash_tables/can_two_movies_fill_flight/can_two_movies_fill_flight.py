def can_two_movies_fill_flight(movie_lengths, flight_length):
  movies = {}

  for length in movie_lengths:
    pair_length = flight_length - length
    if pair_length in movies.keys():
      return True 
    
    movies[length] = pair_length
  
  return False

  # Can also use a set()
  # set.add
  # item in set