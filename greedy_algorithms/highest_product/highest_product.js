// given list of integers, calculate the highest product possible from 3 numbers
// I can try to be greedy
// Keep track of the 3 largest numbers
// at current index, check if this number is greater than the smallest of the 3 numbers and update
// function highestProductOf3(arrayOfInts) {

//   // Calculate the highest product of three numbers
//   if (arrayOfInts.length < 3) { throw new Error("Must be at least 3 integers"); }

//   const threeBiggestNumbers = [ arrayOfInts[0], arrayOfInts[1], arrayOfInts[2]];
//   let maxProduct = arrayOfInts[0] * arrayOfInts[1] * arrayOfInts[2];

//   for (let i = 3; i < arrayOfInts.length; i++) {
//     const currNumber = arrayOfInts[i];

//     const smallestNumber = Math.min(threeBiggestNumbers[0], threeBiggestNumbers[1], threeBiggestNumbers[2]);
//     for (let j = 0; j < 3; j++) {
//       const comparedNumber = threeBiggestNumbers[j];
//       // get the new product by replacing this comparedNumber with our currNumber
//       const potentialProduct = (maxProduct / comparedNumber) * currNumber;
//       // if (currNumber > comparedNumber && comparedNumber === smallestNumber) {
//       // need to consider negative values; just because the current number is larger and we are greedy
//       // we still have to check if the PRODUCT is truly bigger
//       if (potentialProduct > maxProduct) {
//         // replace comparedNumber in our array with the currNumber since product is bigger
//         threeBiggestNumbers[j] = currNumber;
//         maxProduct = potentialProduct;
//         // break;
//       }
//     }

//   }

//   let output = 1;
//   for (let number of threeBiggestNumbers) {
//     output *= number;
//   }

//   return output;
// }

function highestProductOf3(arrayOfInts) {
  // Just wanted fresh slate
  if (arrayOfInts.length < 3) { throw new Error("Must have at least 3 integers"); }

  // GREEDY?
  // keep track of a largest product 
  // in order to do so, we need to save the largest number
  // then check if the current number when multiplied by the largest product of 2 is greater than the saved largest product
  // but also need to keep track of the most negative product of 2 in case our current value is negative
  // then we can check if current num x lowest or current num x highest product of 2 is larger than our saved largest product
  // but we also need to update the current highest product and lowest product of 2
  // we can do so by keeping track of the smallest and biggest number
  let highest_product_of_3 = arrayOfInts[0] * arrayOfInts[1] * arrayOfInts[2];
  let lowest = arrayOfInts[0] <= arrayOfInts[1] ? arrayOfInts[0] : arrayOfInts[1];
  let highest = arrayOfInts[0] <= arrayOfInts[1] ? arrayOfInts[1] : arrayOfInts[0];
  let highest_product_of_2 = arrayOfInts[0] * arrayOfInts[1];
  let lowest_product_of_2 = arrayOfInts[0] * arrayOfInts[1];
  
  for (let i = 2; i < arrayOfInts.length; i++) {
    const currentVal = arrayOfInts[i];
    
    // updating the highest_product_of_3
    if (highest_product_of_2 * currentVal > highest_product_of_3) {
      highest_product_of_3 = highest_product_of_2 * currentVal;
    } 
    if (lowest_product_of_2 * currentVal > highest_product_of_3) {
      highest_product_of_3 = lowest_product_of_2 * currentVal;
    }

    // in the next iterated element, we need to keep the highest and lowest product of 2 updated!
    // Try both the highest and lowest vals with the currentVal!
    if (highest * currentVal > highest_product_of_2) {
      highest_product_of_2 = highest * currentVal;
    } 
    if (lowest * currentVal > highest_product_of_2) {
      highest_product_of_2 = lowest * currentVal;
    }
    if (lowest * currentVal < lowest_product_of_2) {
      lowest_product_of_2 = lowest * currentVal;
    }
    if (highest * currentVal < lowest_product_of_2) {
      lowest_product_of_2 = highest * currentVal;
    }

    // finally update lowest and highest for user in the next element
    // am i lower than the min, am i greater than the max?
    if (currentVal < lowest) {
      lowest = currentVal;
    } 
    if (currentVal > highest) {
      highest = currentVal;
    }

  }

  return highest_product_of_3;
}

const array = [-10, 1, 3, 2, -10];
// console.log(highestProductOf3(array));


// console.log(highestProduct(array));
console.log(highestProduct([-5, -1, -3, -2]));