#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const string = process.argv[3];
fs.writeFile(path, string, 'utf-8', (err, data) => {
  if (err) console.error(err);
  console.log(data);
});
