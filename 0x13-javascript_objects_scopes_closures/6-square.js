#!/usr/bin/node
class Square extends require('./5-square') {
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
