#!/usr/bin/node
if (process.argv.length < 4) {
    console.log('0');
  } else {
    const data = process.argv.slice(2);
    data.sort((i, j) => j - i);
    console.log(data[1]);
  }
