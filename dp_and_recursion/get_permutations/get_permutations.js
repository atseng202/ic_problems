function getPermutations(string) {

  // Generate all permutations of the input string
  if (string.length <= 1) {
    return new Set([string]);
  }

  let word_without_last_letter = string.slice(0, string.length - 1);
  let last_letter = string[string.length - 1];
  previous_permutation = getPermutations(word_without_last_letter);

  const updated_set = new Set();
  for (let word of previous_permutation) {
    for (let i = 0; i < word.length + 1; i++) {
      const new_word = word.slice(0, i) + last_letter + word.slice(i, word.length);
      updated_set.add(new_word);
    }
  }

  return updated_set;

}
   

// empty string = return empty set
// string count of 1 = return set with that char

let input = '';
input = 'a';
input = 'abc';
console.log(getPermutations(input));
