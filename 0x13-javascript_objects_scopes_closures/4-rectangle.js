#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0;
      this.height = 0;
    }
  }

  print () {
    let rec = '';
    for (let n = 0; n < this.height; n++) {
      for (let idx = 0; idx < this.width; idx++) {
        rec += 'X';
      }
      rec += '\n';
    }
    process.stdout.write(rec);
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}
module.exports = Rectangle;
