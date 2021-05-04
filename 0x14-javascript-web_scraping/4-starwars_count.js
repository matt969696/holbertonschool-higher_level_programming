#!/usr/bin/node
/* Task 3 */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jO = JSON.parse(body);
    let total = 0;
    for (let i = 0; i < jO.count; i++) {
      for (let j = 0; j < jO.results[i].characters.length; j++) {
        if (jO.results[i].characters[j].includes('18')) {
          total++;
        }
      }
    }
    console.log(total);
  }
});
