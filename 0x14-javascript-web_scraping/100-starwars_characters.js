#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/3';
request(url, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body).characters;
    for (const dt of data) {
      request(dt, (err, response, body) => {
        if (!err) {
          const char = JSON.parse(body);
          console.log(char.name);
        }
      });
    }
  }
});
