#!/usr/bin/node
const dict = require('./101-data').dict;
const counterDict = {};
for (const [id, num] of dict.entries()){
    if (num in counterDict){
        counterDict[num].push(id);
    } else {
        counterDict[num] = id;
    }
}
console.log(counterDict);
