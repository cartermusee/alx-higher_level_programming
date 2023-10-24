#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, (err, response, body) => {
  if (!err) {
    const todos = JSON.parse(body);
    const complete = {};

    for (const todo of todos) {
      if (todo.completed) {
        const userid = todo.userId;
        if (complete[userid]) {
          complete[userid]++;
        } else {
          complete[userid] = 1;
        }
      }
    }
    console.log(complete);
  }
});
