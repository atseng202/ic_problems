// Write a function mergeRanges() that takes an array of multiple meeting time ranges and 
// Returns an array of condensed ranges

/*
Example:
Given:
  [
  { startTime: 0,  endTime: 1 },
  { startTime: 3,  endTime: 5 },
  { startTime: 4,  endTime: 8 },
  { startTime: 10, endTime: 12 },
  { startTime: 9,  endTime: 10 },
]
returns:
  [
  { startTime: 0, endTime: 1 },
  { startTime: 3, endTime: 8 },
  { startTime: 9, endTime: 12 },
]
*/

// Plan: I want to go through each range and check its startTime and endTime
// 1. Sort the ranges by their startTime and endTime (nlgn)
// 2. Then do a loop over the newly sorted array and check for
// 2a. if the upcoming startTime is within the endTime of the previous range; if it is like 4 is before 5, then update the endtime to include the current endTime
// 2b. if the upcoming startTime is after the previous endTime, we can add the previous start and endTime into our final array
// Ex. 0 and 1 are the previous start and endTimes, 3 is after 1, so we add 0 and 1 as a range and then update the current range to be 3 and 5
// then we check 4 and 4 is within the endTime of 5, so we update the previous endTime to be 8 and keep 3
// 9 is after the previous endTime of 8 so add range of 3 - 8 into the final array
// 10 is within the endTime of 10, so we update the new endTime to be 12
// When we reach the end of the array, push the final current start and endtimes to the final array
// and return the array

// Helper function to sort the ranges in increasing order
function sortRanges(rangesArr) {
  let sortedRangesArr = rangesArr.slice(0).sort( (firstRange, nextRange) => {
    if (firstRange.startTime < nextRange.startTime) {
      // if the startTime of the first one is less than the second one 
      return -1;
    } else if (firstRange.startTime === nextRange.startTime) {
      // if the startTimes are equal, we compare their endTimes
      if (firstRange.endTime < nextRange.endTime) { 
        return -1;
      } else if (firstRange.endTime > nextRange.endTime) {
        // endTime is bigger?
        return 1;
      } else {
        // endTimes are equal?
        return 0;
      }
    } else {
      // firstRange startTime is > nextRange startTime
      return 1;
    }
  });
  return sortedRangesArr;
}

// Time complexity: nlgn to sort + O(n) to iterate over the ranges again and get a final array;
// Space complexity: Also O(n) to create the sorted array and also to return a new array;
function mergeRanges(rangesArr) {
  // sort the array by start and endtimes, making sure each upcoming starttime is before the next one
  // and each endtime is less than or equal to the next one
  const sortedRangesArr = sortRanges(rangesArr);

  const finalRanges = [];
  let prevStartTime; 
  let prevEndTime;
  let rangeLength = sortedRangesArr.length;
  // 2. loop over the array and keep track of the prev start and endTimes and compare with the current times
  sortedRangesArr.forEach( (range, idx) => {
    const currentStartTime = range.startTime;
    const currentEndTime = range.endTime;

    if (!prevStartTime && !prevEndTime) {
      prevStartTime = currentStartTime;
      prevEndTime = currentEndTime;
    } else if (currentStartTime <= prevEndTime) {
      // current starting time is within the range of the previous endtime so we update the range constraints
      prevEndTime = ( prevEndTime > currentEndTime ? prevEndTime : currentEndTime);
    } else {
      // currentStartTime is > than, or out of range of the prevEndTime, so we need to add that previous range into our final output
      finalRanges.push({ startTime: prevStartTime, endTime: prevEndTime });
      // then update the prev start and endtimes to the current one;
      prevStartTime = currentStartTime;
      prevEndTime = currentEndTime;
    }

    // finally, if we reach the end ot the array, we have to update the latest start and end times!
    if (idx === rangeLength - 1) {
      finalRanges.push({startTime: prevStartTime, endTime: prevEndTime});
    }
  }); 

  return finalRanges;
}

// console.log(mergeRanges([
//   { startTime: 0, endTime: 1 },
//   { startTime: 3, endTime: 5 },
//   { startTime: 4, endTime: 8 },
//   { startTime: 10, endTime: 12 },
//   { startTime: 9, endTime: 10 },
// ]));

// console.log(mergeRanges([{ startTime: 1, endTime: 8 }, { startTime: 2, endTime: 5 }]));
console.log(mergeRanges([
  { startTime: 1, endTime: 10 },
  { startTime: 2, endTime: 6 },
  { startTime: 3, endTime: 5 },
  { startTime: 7, endTime: 9 },
]));