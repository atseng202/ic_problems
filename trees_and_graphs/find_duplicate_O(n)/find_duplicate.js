function findDuplicate(intArray) {

  // Find a number that appears more than once ... in O(n) time
  // consider each number to be a linked list node, pointing to the value-eth node 
  // 1 points to position 1, 2 to position 2, 5 to position 5
  // my thought process is to iterate thru the list
  // and swap the values if the current index is not at the right value
  // if it is do nothing
  // if it isn't then check the position to swap
  // if the position to swap with is an equal value, we return that value since it means its a duplicate

  for (let i = 0; i < intArray.length; i++) {
    const currValue = intArray[i];

    const position = i + 1;
    if (currValue !== position) {
      // the current value is not in the correct position, so check the position to swap with
      // position is the current value, index is currValue - 1
      const valueToSwapWith = intArray[currValue - 1];
      if (currValue === valueToSwapWith) {
        return currValue;
      } else {
        // swap the two values
        intArray[i] = valueToSwapWith;
        intArray[currValue - 1] = currValue;
      }
    }
  }

  return 0;
}

function findDup(intArray) {
  // first get inside the cycle starting from the head of the node, aka the last value in the array
  // if we traverse n values, we will be inside the cycle
  // a cycle exists where multiple nodes points to the same value
  let maxDistinctNums = intArray.length - 1;

  let currPosition = maxDistinctNums + 1;
  for (let i = 0; i < maxDistinctNums; i++) {
    currPosition = intArray[currPosition - 1];
  }

  // currPosition is guaranteed to be in the cycle
  // need to get the length of the cycle so that we separate the head from a node that is the length of the cycle
  // then traverse a certain number of steps until both nodes are equal
  // the head of the cycle is the dup, since multiple nodes point to it
  let savedPositionInCycle = currPosition;
  let cycleCount = 1;
  let currPositionInCycle = intArray[savedPositionInCycle - 1];

  while (currPositionInCycle !== savedPositionInCycle) {
    currPositionInCycle = intArray[currPositionInCycle - 1];
    cycleCount += 1;
  }

  let headStart = maxDistinctNums + 1;
  let aheadStart = maxDistinctNums + 1;
  for (let i = 0; i < cycleCount; i++) {
    aheadStart = intArray[aheadStart - 1];
  }

  // move step by step until they are equal
  while (headStart !== aheadStart) {
    headStart = intArray[headStart - 1];
    aheadStart = intArray[aheadStart - 1];
  }

  return headStart;
}

console.log(findDup([1,2,2,3,4]));
