#!/usr/bin/node
/* Task 6 */

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jO = JSON.parse(body);
    const dict = {};
    for (let i = 0; i < jO.length; i++) {
      if (!(jO[i].userId in dict) && jO[i].completed === true) {
        dict[jO[i].userId] = 0;
      }
      if (jO[i].completed === true) {
        dict[jO[i].userId] += 1;
      }
    }
    console.log(dict);
  }
});
