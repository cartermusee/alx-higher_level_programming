#!/usr/bin/node
const x = process.argv[2];
const num1 = parseInt(x);
if (parseInt(num1)){
    for (let i = 0; i < x; i++){
        console.log('c is fun');
    }
}
else{
    console.log('Missing number of occurrences')
}
