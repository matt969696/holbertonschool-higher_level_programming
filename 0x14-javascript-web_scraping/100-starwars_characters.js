#!/usr/bin/node
/* Task 3 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jO = JSON.parse(body);
    for (let i = 0; i < jO.characters.length; i++) {
      const charurl = jO.characters[i];
      request(charurl, function (error, response, body) {
        if (error) {
          console.log(error);
        } else {
          const jC = JSON.parse(body);
          console.log(jC.name);
        }
      });
    }
  }
});
