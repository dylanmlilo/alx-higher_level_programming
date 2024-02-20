#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;
const charUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const count = films.filter(film => film.characters.includes(charUrl)).length;
    console.log(count);
  } else {
    console.error(error);
  }
});
