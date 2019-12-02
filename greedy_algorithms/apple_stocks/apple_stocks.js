// array of stockPrices where indices are time in minutes past opening trade time of 9:30 AM local time
// values are price of one share of Apple stock at that time
// If $500 at 10:30 AM, then stockPrices[60] = 500

// Take stockPrices and return the best profit you could make from one purchase and one sale of one share of Apple stock the day before
// const stockPrices = [10, 7, 5, 8, 11, 9];
// getMaxProfit(stockPrices);
// Returns 6 (buying for $5 and selling for $11)

// Greedy: take the lowest possible share price and then locate the highest possible share price after that index
// But that is not guaranteed to be the best profit 

// Brute force: I can make a hash, and brute force it 
// Iterate thru every other item, and compare it to first item 
// Get the best possible profit for 10
// then do the same for 7 and everything else
// finally, iterate thru the array 1 more time, and check for the best profit
function getMaxProfit(stockPrices) {
  const stocksLength = stockPrices.length;
  if (stocksLength <= 1) {
    throw new Error("Must have more than 1 stock");
  }

  const bestProfitsHash = {};
  for (let i = 0; i < stocksLength - 1; i++) {
    const currStock = stockPrices[i];

    for (let j = i + 1; j < stocksLength; j++) {
      // compare with the currStock for current difference
      const comparedStock = stockPrices[j];
      const stockDifference = comparedStock - currStock;
      if (bestProfitsHash[currStock]) {
        // previously updated with a highest stock so check which one is bigger
        bestProfitsHash[currStock] = Math.max(stockDifference, bestProfitsHash[currStock]);
      } else {
        // never added a highest profit stock
        bestProfitsHash[currStock] = stockDifference;
      }
    }
  }

  let bestPossibleProfit;
  stockPrices.forEach( (price, idx) => {
    if (idx < stocksLength - 1) {
      // only consider the prices before the last one

      // iterate one more time to find the best possible profit
      if (!bestPossibleProfit) {
        bestPossibleProfit = bestProfitsHash[price];
      } else {
        // compare bestPossible profit with what is currently in the hash
        bestPossibleProfit = Math.max(bestProfitsHash[price], bestPossibleProfit);
      }
    }
  });

  return bestPossibleProfit;
}

function getMaxProfit_better(stockPrices) {
  // try to do it in one pass
  // keep track of the smallest number at each index at the very end of loop
  // use the smallest number to compare with the current index for max profit
  // get max profit by comparing with current profit and what was stored max profit
  // done
  const stocksCount = stockPrices.length;
  if (stocksCount <= 1) { throw new Error("Must have more than 1 stock"); }

  let smallestNumber = stockPrices[0];
  let maxProfit;
  for (let i = 1; i < stocksCount; i++) {
    // now get curr profit
    const currPrice = stockPrices[i];
    const currProfit = currPrice - smallestNumber;

    if (!maxProfit) {
      maxProfit = currProfit;
    } else {
      maxProfit = Math.max(currProfit, maxProfit);
    }

    // update the smallest stock
    smallestNumber = Math.min(currPrice, smallestNumber);
  }

  return maxProfit;
}


// const stockPrices = [10, 7, 5, 8, 11, 9];
// const stockPrices = [1, 5, 3, 2];
// const stockPrices = [7, 2, 8, 9];
// const stockPrices = [1, 6, 7, 9]; 
// const stockPrices = [9, 7, 4, 1];
// const stockPrices = [1, 1, 1, 1];

console.log(getMaxProfit_better(stockPrices));

