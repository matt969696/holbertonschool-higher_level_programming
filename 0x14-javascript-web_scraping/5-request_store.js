#!/usr/bin/node
/* Task 5 */

const fs = require('fs');
const url = process.argv[2];
const doc = process.argv[3];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(doc, body, 'utf-8', (err, data) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
