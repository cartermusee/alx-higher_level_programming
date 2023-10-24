#!/usr/bin/node

const request = require('request');
const id = 18;
let count = 0;
const url = process.argv[2];
request(url, (error, response, body) => {
  if (!error) {
    const films = JSON.parse(body).results;
    for (const film of films) {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${id}/`)) {
        count++;
      }
    }
    console.log(count);
  } else {
    console.error(error);
  }
});
