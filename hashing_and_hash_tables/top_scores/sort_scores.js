// Players receive score between 0 and 100, our algorithm is nlgn and players
// complain that rankings don't update fast enough 
// Write a function taking 
// 1. an array of unsortedScores
// 2. highestPossibleScore in the game
// Returns: a sorted array of scores in less than O(nlgn) time
// Example:
// const unsortedScores = [37, 89, 41, 65, 91, 53];
// const HIGHEST_POSSIBLE_SCORE = 100;

// sortScores(unsortedScores, HIGHEST_POSSIBLE_SCORE);
// returns [91, 89, 65, 53, 41, 37]

// Plan: Use a hash?
// iterate thru the unsortedScores
// Hint says to build an array of scoreCounts
// indices represent the scores, values represent the number of times the scores appear
// this makes alot of sense
function sortScores(unsortedScores, highestPossibleScore) {

  const scoresMap = new Map();
  for (let score of unsortedScores) {
    if (scoresMap.has(score)) {
      scoresMap.set(score, scoresMap.get(score) + 1);
    } else {
      // new score 
      scoresMap.set(score, 1);
    }
  }

  const scores = [];
  for (let i = highestPossibleScore; i >= 0; i--) {
    if (scoresMap.has(i)) {
      const frequencyOfScore = scoresMap.get(i);
      for (let j = 0; j < frequencyOfScore; j++) {
        scores.push(i);
      }
    }
  }

  return scores;
}

const unsortedScores = [37, 89, 41, 65, 91, 53];
const HIGHEST_POSSIBLE_SCORE = 100;

console.log(sortScores(unsortedScores, HIGHEST_POSSIBLE_SCORE));