#!/usr/bin/node
const x = process.argv[2];
const num1 = parseInt(x);
if (num1) {
  for (let i = 0; i < num1; i++) {
    console.log('c is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
