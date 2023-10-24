#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const stri = process.argv[3];
fs.writeFile(path, stri, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
