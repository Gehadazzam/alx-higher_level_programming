#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let rec = '';
    for (let n = 0; n < this.height; n++) {
      for (let idx = 0; idx < this.width; idx++) {
        rec += c;
      }
      rec += '\n';
    }
    process.stdout.write(rec);
  }
}
module.exports = Square;
