// Reverse a given array of characters in place 
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

let arr = [1,2,3,4,5];
console.log(arr);
reverse(arr);
console.log(arr);