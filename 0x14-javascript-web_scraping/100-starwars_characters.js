#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (err, response, body) => {
  if (err) console.error(err);
  const characters = JSON.parse(body).characters;
  characters.forEach((character) => {
    request(character, (err, response, body) => {
      if (err) console.error(err);
      console.log(JSON.parse(body).name);
    });
  });
});
