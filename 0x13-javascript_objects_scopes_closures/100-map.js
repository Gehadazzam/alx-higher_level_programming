#!/usr/bin/node
const list = require('./100-data').list;
console.log(list);
const mulitList = list.map((num, idx) => num * idx);
console.log(mulitList);
