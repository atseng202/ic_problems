function fib(n) {
  if (n < 0) {
    throw new ValueError("Cannot have neg inputs");
  }

  if (n <= 1) { return n; }

  let prevVal = 1;
  let prevPrevVal = 0;

  for (let i = 2; i <= n; i++) {
    let current = prevVal + prevPrevVal;
    prevPrevVal = prevVal;
    prevVal = current;
  }

  return prevVal;
}