#!/usr/bin/node
const arg = process.argv[2];
const numOcurrence = parseInt(arg);
if (isNaN(numOcurrence)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numOcurrence; i++) {
    console.log('C is fun');
  }
}
