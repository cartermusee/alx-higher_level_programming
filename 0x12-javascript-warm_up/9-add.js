#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  return Number(a) + Number(b);
}

console.log(add(a, b));
