// Takes an integer flightLength
// from an array of moveLengths, return a boolean indicating
// whether there are two numbers in moveLengths whose sum equals flightLength

// plan: iterate over the movie lengths
// update: Using a hash
// I iterate over the array and check for any complimentary value to this current length in the array
// if it exists in the hash it means I have added a complimentary movie into the hash and therefore two movies exist that add up
// to flightLength
// at the end of each loop I add the movie length into the hash with its complimentary value as the key's value

// New note: Could also use a new Set()
// set.add new items
// check if a set.has(item)
function canTwoMoviesFillFlight(movieLengths, flightLength) {
  const movies = {};
  for (const length of movieLengths) {
    const pairLength = flightLength - length;
    if (movies[pairLength]) {
      // this movie's pair was added before in the hash 
      return true;
    }
    movies[length] = pairLength;
  }
  return false;
}