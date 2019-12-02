// take an array of characters with a space separating one word from another
// reverses the array, not all the characters so that: 
// [ 'c', 'a', 'k', 'e', ' ',
// 'p', 'o', 'u', 'n', 'd', ' ',
  // 's', 't', 'e', 'a', 'l' ];
// becomes:
// 'steal pound cake' when joined

// const arr = ['l', 'a', 'e', 't', 's', ' ', ' d', 'n', 'u', 'o', 'p', ' ', 'e', 'k', 'a', 'c'];
// helper
function reverse(stringArr) {
  let firstIdx = 0;
  let lastIdx = stringArr.length - 1;

  while (firstIdx < lastIdx) {
    const latestChar = stringArr[lastIdx];
    stringArr[lastIdx] = stringArr[firstIdx];
    stringArr[firstIdx] = latestChar;
    firstIdx++;
    lastIdx--;
  }
}

function reverseWords(words) {
  // plan: reverse the entire arr, then reverse the words for each slice up until each empty space
  reverse(words);

  let currStartIdx = 0;
  let currEndIdx; 
  for (let i = 0; i < words.length; i++) {
    if ((words[i] === " ")) {
      // console.log(i);
      currEndIdx = i;
      // now reverse all the words from start to end index exclusive
      while (currStartIdx < currEndIdx - 1) {
        const latestChar = words[currEndIdx - 1];
        words[currEndIdx - 1] = words[currStartIdx];
        words[currStartIdx] = latestChar;
        currStartIdx++;
        currEndIdx--;
      }
      // now reset 
      currStartIdx = i + 1;
    }
  }

  // handle final case 
  if (currStartIdx < words.length - 1) {
    currEndIdx = words.length - 1;
    while (currStartIdx < currEndIdx) {
      const latestChar = words[currEndIdx];
      words[currEndIdx] = words[currStartIdx];
      words[currStartIdx] = latestChar;
      currStartIdx++;
      currEndIdx--;
    }
  }
}

const message = ['c', 'a', 'k', 'e', ' ',
  'p', 'o', 'u', 'n', 'd', ' ',
  's', 't', 'e', 'a', 'l'];

// reverse(message);
// console.log(message);

reverseWords(message);

console.log(message.join(''));
