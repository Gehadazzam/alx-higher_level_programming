#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(url, (err, response, body) => {
  if (err) console.error(err);
  const movieData = JSON.parse(body);
  if (!movieData.title) console.error('not found');
  console.log(movieData.title);
});
