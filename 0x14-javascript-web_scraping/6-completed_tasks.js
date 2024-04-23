#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';
const tracker = {};
request.get(url, (err, response, body) => {
  if (err) console.error(err);
  const all = JSON.parse(body);
  for (let p = 0; p < all.length; p++) {
    const userId = all[p].userId;
    const completed = all[p].completed;
    if (!tracker[userId] && completed) {
      tracker[userId] = 0;
    }
    if (completed) tracker[userId]++;
  }
  console.log(tracker);
});
