#!/usr/bin/node
function factorial (val) {
  if (isNaN(val) || val < 0) {
    return 1;
  } else if (val === 1 || val === 0) {
    return 1;
  } else {
    return val * factorial(val - 1);
  }
}

const arg1 = process.argv[2];

const arg1Parsed = parseInt(arg1);

console.log(factorial(arg1Parsed));
