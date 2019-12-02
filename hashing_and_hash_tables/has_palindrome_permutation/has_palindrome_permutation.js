// Check if any permutation of the input string is a palindrome
// Strategy:
// Brute force would be: try to change the string into a palindrome
// if I can do it it is true
// for a palindrome, if the string is even, then each character should
// have an even count 
// for an odd string, then each character should be even except one character

function hasPalindromePermutation(theString) {

  // Check if any permutation of the input is a palindrome
  const charactersCount = {};

  for (let char of theString) {
    if (charactersCount[char]) {
      charactersCount[char] += 1;
    } else {
      // new character, add it in
      charactersCount[char] = 1;
    }
  }

  // built the hash, now I can use it to make sure that all the 
  // 
  // const isEven = (theString.length % 2 === 0);
  // Don't need to check even or odd bc at best, there should be only 1 odd count
  // for even strings, 0 odd frequencies
  // ofc for even strings we can short circuit in the loop 
  // and return false if there is an odd frequency given we know the string is even
  // but this is a premature optimization!
  let freqOfOddCounts = 0;
  for (let key in charactersCount) {
    if (charactersCount.hasOwnProperty(key)) {
      // now check for freq of odd counts
      if (charactersCount[key] % 2 !== 0) {
        freqOfOddCounts += 1;
      }
    }
  }

  return freqOfOddCounts <= 1;
}