// This is a Knuth shuffle
// Get a random index from n items, and swap at current index
// Then get a random index from n - 1 items, and swap
// and so forth because every value has a probability of 1/n of getting picked in this way
function getRandom(floor, ceiling) {
  return Math.floor(Math.random() * (ceiling - floor + 1)) + floor;
}

function shuffle(array) {

  arr_length = array.length;
  // Shuffle the input in place
  for (let i = 0; i < array.length; i++) {
    const curr_val = array[i];
    const random_idx = getRandom(i, arr_length - 1);
    if (random_idx !== i) {
      array[i] = array[random_idx];
      array[random_idx] = curr_val;
    }
    
  }
}

const sample = [1, 2, 3, 4, 5];
console.log('Initial array: ', sample);
shuffle(sample);
console.log('Shuffled array: ', sample);