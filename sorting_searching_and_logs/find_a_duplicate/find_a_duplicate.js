function findRepeat(numbers) {

  // Find a number that appears more than once
  // if I sort the array first (O(nlgn)), then I can just iterate thru the array one more time to get the repeat
  // space complexity: O(1), time complexity: O(nlgn) since its O(n) to find the dup but the sort takes nlgn

  numbers.sort();
  for (let i = 0; i < numbers.length - 1; i++) {
    let currNumber = numbers[i];
    let nextNumber = numbers[i+1];
    if (currNumber == nextNumber) {
      return currNumber;
    }
  }

}

function findRepeatKeepInputSame(numbers) {
  // Using needle in haystack
  // in the problem there are distinct numbers from 1 to n, and the total number of items is n + 1
  // that means if we split the array into subarrays of range (1...n/2) and (n/2 + 1...n)
  // sum of the distinct numbers for the subarray ranges will be n 
  // sum of the numbers count in the subarrays will be n + 1
  // it is understood that within any range, the count of numbers in that range will be n+1 while the 
  // number of distinct numbers will be n so there will be 1 or more duplicates in that range
  // using binary search, I can restrict the range and check the number of items in that range and if I
  // can find more numbers than the biggest number in that range, then I use use that floor and ceiling
  // until I compare a floor and ceiling of size 1, in which case I've found the number

  // smallest number is floor, biggest number is ceiling aka n
  let floor = 1;
  let ceiling = numbers.length - 1;

  while (floor < ceiling) {
    let midpoint = Math.floor( floor + (ceiling - floor) / 2);
    let lowerFloor = floor;
    let lowerCeiling = midpoint;
    let higherFloor = midpoint + 1;
    let higherCeiling = ceiling;

    const distinctNumberOfItemsInLowerRange = lowerCeiling - lowerFloor + 1;

    let numberOfItemsInLowerRange = 0;
    numbers.forEach((num) => {
      if (num >= lowerFloor && num <= lowerCeiling) {
        numberOfItemsInLowerRange += 1;
      }
    });


    if (numberOfItemsInLowerRange > distinctNumberOfItemsInLowerRange) {
      floor = lowerFloor;
      ceiling = lowerCeiling;
    } else {
      floor = higherFloor;
      ceiling = higherCeiling;
    }
  }

  return floor;
}