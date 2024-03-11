#!/usr/bin/node
const args = process.argv.length;
if (args < 4) {
  console.log('0');
} else {
  const num = process.argv.slice(2);
  const sortNum = num.map(Number).sort((x, z) => z - x);
  console.log(sortNum[1]);
}
