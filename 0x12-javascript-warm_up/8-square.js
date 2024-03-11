#!/usr/bin/node
const arg = process.argv[2];
const size = parseInt(arg);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let width = 0; width < size; width++) {
    for (let height = 0; height < size; height++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
