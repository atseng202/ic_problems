// find the rotation point of the array, given that words start somewhere in the middle of the array and then 
// suddenly starts at the beginning of the dictionary after
// Scenarios if I binary search:
// 1. If the word in the middle index is between a word bigger than it before, and a word bigger than it after, this is the word
// 2. If the word is smaller than the first word in the array but is in increasing order like a, b, c, we have to cut off the words after it for binary search
// 3. If the word is bigger than the first word in the array, then we cut off all words before and including it 
function findRotationPoint(words) {
  if (words.length < 2) { throw new Error("No rotation point if less than 2 words"); }
  // Find the rotation point in the vector
  // let first_index = 0;
  let floor_index = 0;
  let ceiling_index = words.length;

  // console.log(words);
  while (floor_index  < ceiling_index) {
    const half_distance = Math.floor((ceiling_index - floor_index) / 2); 
    const middle_index = floor_index + half_distance;
    const middle_word = words[middle_index];
    
    const index_before = middle_index - 1;
    const index_after = middle_index + 1;
    const potential_word_before = words[index_before];
    const potential_word_after = words[index_after];
  // compare middle word with the word before and after
    // it is okay for a word before to not exist or a word after to not exist aka only 2 words 
    if (potential_word_before && potential_word_after && middle_word < potential_word_before && middle_word < potential_word_after) {
      return middle_index;
    } else if (potential_word_before && !potential_word_after && middle_word < potential_word_before) {
      return middle_index;
    } else if (potential_word_after && !potential_word_before && potential_word_after < middle_word) {
      return index_after;
    } 

    // now check the scenarios I talked about
    // 1. middle_word is smaller than first word in array but is in increasing order like first word: 'pokemon', and current_word: 'banana'
    // but 'banana' is between 'back' and 'cap', so we cut off all the words after this word
    if (middle_word < words[0] && (!potential_word_before || (potential_word_before && middle_word > potential_word_before))  && (!potential_word_after || (potential_word_after && middle_word < potential_word_after))) {
      // cut off all the words after this word
      ceiling_index = middle_index;
    } else if (middle_word > words[0]) {
      floor_index = middle_index;
    }

  }

  return -1;
}

const words = ['ptolemaic', 'retrograde', 'supplant',
  'undulate', 'xenoepist', 'asymptote',
  'babka', 'banoffee', 'engender',
  'karpatka', 'othellolagkage'];

console.log(findRotationPoint(words));