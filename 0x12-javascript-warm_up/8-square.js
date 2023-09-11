#!/usr/bin/node
const size = process.argv[2];
const num1 = parseInt(size);
if (isNaN(num1)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let y = 0; y < size; y++) {
      row += 'X';
    }
    console.log(row);
  }
}
