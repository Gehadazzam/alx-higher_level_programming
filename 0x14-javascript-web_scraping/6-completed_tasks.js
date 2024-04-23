#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const tracker = {};
request.get(url, (err, response, body) => {
  if (err) console.error(err);
  const all = JSON.parse(body);
  for (let p = 0; p < all.length; p++) {
    const completed = all[p].completed;
    if (completed) {
      if (tracker[all[p].userId] === undefined) {
        tracker[all[p].userId] = 1;
      } else {
        tracker[all[p].userId] += 1;
      }
    }
  }
  console.log(tracker);
});
