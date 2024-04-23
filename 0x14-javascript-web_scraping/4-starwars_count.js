#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const count = 0
const id = 18
request.get(url, (err, response, body) => {
  if (err) console.error(err);
  const data = JSON.parse(body);
  
});
