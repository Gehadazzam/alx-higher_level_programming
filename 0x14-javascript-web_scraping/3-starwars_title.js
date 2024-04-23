#!/usr/bin/node

const request = require('request');
const movieid = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieid}`;
request.get(url, (err, response, body) => {
  if (err) console.error(err);
  const movieData = JSON.parse(body);
  if (!movieData.title) console.error('not found');
  console.log(movieData.title);
});
