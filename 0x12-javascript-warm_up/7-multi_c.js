#!/usr/bin/node
const x = process.argv[2];
const num1 = parseInt(x);
if (isNaN(num1)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('c is fun');
  }
}
