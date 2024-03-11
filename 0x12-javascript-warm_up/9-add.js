#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}

const firstArg = process.argv[2];
const seconedArg = process.argv[3];
const firstNum = parseInt(firstArg);
const seconedNum = parseInt(seconedArg);
if (isNaN(firstNum) || isNaN(seconedNum)) {
  console.log('NaN');
} else {
  add(firstNum, seconedNum);
}
