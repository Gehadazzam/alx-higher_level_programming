#!/usr/bin/node
function getFactorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  } else if (num > 1) {
    return num * getFactorial(num - 1);
  }
}
const args = process.argv[2];
const number = parseInt(args);
if (isNaN(number)) {
  console.log('1');
} else {
  console.log(getFactorial(number));
}
