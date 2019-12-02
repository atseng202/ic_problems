// Given array of ints, return an array of products at that index that include all the other integers 
// except the one at that index

// Brute force: I iterate through all other numbers to multiply?
function getProductsOfAllIntsExceptAtIndex(intArray) {
  if (intArray.length < 2) { throw new Error("Array must have 2 more more ints"); }

  // Make a list of the products
  const output = [];
  for (let i = 0; i < intArray.length; i++) {
    const current = intArray[i];

    let product = 1;
    for (let j = 0; j < intArray.length; j++) {
      if (j !== i) {
        product *= intArray[j];
      }
    }
    output.push(product);
  }

  return output;
}

const arr = [4, 3, 9, 1, 2];
// console.log(getProductsOfAllIntsExceptAtIndex(arr));
const answer = [3 * 9 * 1 * 2, 4 * 9 * 1 * 2, 4 * 3 * 1 * 2, 4 * 3 * 9 * 2, 4 * 3 * 9 * 1];

function getProductsOfAllIntsExceptAtIndexBetter(intArray) {
  // Will iterate in one pass, add the key to a hash, and then look at the previous array of values that I add into
  // so that I can have the current value multiply each of the previous values AND for each of the previous values, multiply by the current value

  const productsHash = {};
  const previousVals = [];

  for (let value of intArray) {
    if (!productsHash[value]) {
      productsHash[value] = 1;
    }

    for (let prevValue of previousVals) {
      productsHash[prevValue] *= value;
      productsHash[value] *= prevValue;
    }

    // finally, we add the current value as a previous value 
    previousVals.push(value);
  }

  const products = [];
  for (let value of intArray) {
    const product = productsHash[value]
    products.push(product);
  }

  return products;
}

function getProductsOfAllIntsExceptAtIndexBest(intArr) {
  // so my approach failed to see that there are repeating multiplcations that can be saved 
  // AKA this is the real greedy approach
  // iterate thru array, and save each number
  // at each current number, we can save a product of 2, and then a product of 3, and finally a product of 4
  // save 4
  if (intArr.length < 2) {
    throw new Error("Must have other integers to multiply and not just 1 int");
  }

  let productSoFar = 1;
  let productsSoFarBeforeIndex = [];
  for (let i = 0; i < intArr.length; i++) {
    productsSoFarBeforeIndex[i] = productSoFar;
    productSoFar *= intArr[i];
  } 

  // let productsAfterIndex = [];
  let productAfterSoFar = 1;
  for (let i = intArr.length - 1; i >= 0; i--) {
    // productsAfterIndex[i] = productAfterSoFar;
    // productAfterSoFar *= intArr[i];
    productsSoFarBeforeIndex[i] *= productAfterSoFar;
    productAfterSoFar *= intArr[i];

  }

  return productsSoFarBeforeIndex;
}



// let array = [4, 3, 9, 1, 2];
let array = [2];

console.log(getProductsOfAllIntsExceptAtIndexBest(array));

// let products = [1,4,12,36,]
