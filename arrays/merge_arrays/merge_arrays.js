// Two arrays of orders sorted numerically
// Write function to merge our array of orders into one sorted array

// const myArray = [3, 4, 6, 10, 11, 15];
// const alicesArray = [1, 5, 8, 12, 14, 19];

// console.log(mergeArrays(myArray, alicesArray));
// logs [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

function mergeArrays(firstArray, secondArray) {
  let firstIdx = 0;
  let secondIdx = 0;
  const firstArrLength = firstArray.length;
  const secondArrLength = secondArray.length;

  const mergedArr = [];
  while (firstIdx < firstArrLength && secondIdx < secondArrLength) {
    const firstEle = firstArray[firstIdx];
    const secondEle = secondArray[secondIdx];
    if (firstEle <= secondEle) {
      // smaller or equal so add it into mergedArr first
      mergedArr.push(firstEle);
      firstIdx++;
    } else {
      // add secondEle since it is smaller
      mergedArr.push(secondEle);
      secondIdx++;
    }
  }

  // Final cleanup: check if any of the arrays did not reach the final index
  if (firstIdx < firstArrLength) {
    while (firstIdx < firstArrLength) {
      const ele = firstArray[firstIdx];
      mergedArr.push(ele);
      firstIdx++;
    }
  } else {
    while (secondIdx < secondArrLength) {
      const ele = secondArray[secondIdx];
      mergedArr.push(ele);
      secondIdx++;
    }
  }

  return mergedArr;
}

const myArray = [3, 4, 6, 10, 11, 15];
const alicesArray = [1, 5, 8, 12, 14, 19];

console.log(mergeArrays(myArray, alicesArray));