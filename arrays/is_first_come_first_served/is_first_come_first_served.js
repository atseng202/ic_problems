
// Orders from dine in can be served before take out and vice versa
// but orders within a queue must be first come first served
// aka FIFO 
// keep two pointers and iterate thru the final served array
// check that the current idx for either take out or dine in is equal to the current
// idx we are at for the final array
// increment our pointer indices accordingly
// at any point if a value at either takeOut or dineIn idx is not equal, we know
// the served array is not first come first serve
function isFirstComeFirstServed(takeOutOrders, dineInOrders, servedOrders) {
  // make sure all orders were served
  const takeOutLength = takeOutOrders.length;
  const dineInLength = dineInOrders.length;
  const servedLength = servedOrders.length;
  if (servedLength !== (takeOutLength + dineInLength)) { return false; }
  // Check if we're serving orders first-come, first-served
  let takeOutIdx = 0;
  let dineInIdx = 0;

  // one of the orders will have an undefined value bc the index will increment 
  // to a value > than their array length
  // in python you can't index into an undefined value
  for (let order of servedOrders) {
    const takeOutNumber = takeOutOrders[takeOutIdx];
    const dineInNumber = dineInOrders[dineInIdx];
    if (order === takeOutNumber) {
      takeOutIdx++;
    } else if (order === dineInNumber) {
      dineInIdx++;
    } else {
      // order does not match any of the orders that should be serviced next
     return false; 
    }    
  }
  return true;
}


const takeOut = [1,3,5];
const dineIn = [2,4,6];
const served = [1, 2, 4, 6, 5, 3];
console.log(isFirstComeFirstServed(takeOut, dineIn, served));