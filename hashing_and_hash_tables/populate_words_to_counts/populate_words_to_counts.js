// Take the input string and return the map 
// with the words as keys and the frequency of the word
// as values
// for upper and lowercase versions of the word, they should
// be assumed as the same word

// Brute force: separate the input string into a new array split by " "
// from there, loop over the array, add the lowercased version of each word
// and update its frequency in our map
class WordCloudData {
  constructor(inputString) {
    this.wordsToCounts = new Map();
    this.populateWordsToCounts(inputString);
  }

  // helper methods
  // we need to split all the words into an array, but handle cases like
  // hyphens and non-letters
  splitWords(inputString) {
    const words = [];
    // let newWord = "";
    let wordLength = 0;
    let currWordIndex = 0;
    // if I reach the end of a string, aka a space or hyphen, then slice the array
    // before I made the word, and then added it to the array when i reached a hyphen
    // instead lets try checking for presence of a character first
    for (let i = 0; i < inputString.length; i++) {
      const char = inputString[i];
      if (this.isLetter(char)) {
        // legit letter
        if (wordLength === 0) {
          // start of a new oord
          currWordIndex = i;
        }
        wordLength += 1;

        if (i === inputString.length - 1) {
          // last char and it is a letter!
          // add it into the words array
          const word = inputString.slice(currWordIndex, currWordIndex + wordLength);
          words.push(word);
          wordLength = 0;
        }
      } else {
        // not legit letter but could be end of a sequence
        if (char === " " || char === "-") {
          // is a hyphen or a dash so index up until now is a word
          const word = inputString.slice(currWordIndex, currWordIndex + wordLength);
          words.push(word);
          wordLength = 0;
        }
      
      }

    }
    return words;
  }

  // helper to make sure that the char is a letter
  isLetter(character) {
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.indexOf(character) >= 0;
  }

  populateWordsToCounts(inputString) {

    // Count the frequency of each word
    const wordsArr = this.splitWords(inputString);
    for (let unfilteredWord of wordsArr) {
      const word = unfilteredWord.toLowerCase();
      if (this.wordsToCounts.has(word)) {
        const prevCount = this.wordsToCounts.get(word);
        this.wordsToCounts.set(word, prevCount + 1);
      } else {
        // new word, so set the key, with val of 1
        this.wordsToCounts.set(word, 1);
      }
    }
    return this.wordsToCounts;

  }

}

const data = new WordCloudData("I like cake");
console.log(data.wordsToCounts);