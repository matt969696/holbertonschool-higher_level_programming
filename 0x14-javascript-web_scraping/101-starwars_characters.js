#!/usr/bin/node
/* Task 3 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jO = JSON.parse(body);
    for (let i = 0; i < jO.characters.length; i++) {
      const charurl = jO.characters[i];
      const mybody = await downloadPage(charurl);
      const jC = JSON.parse(mybody);
      console.log(jC.name);
      }
    }
});


function downloadPage (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) reject(error);
      if (response.statusCode != 200) {
        reject('Invalid status code <' + response.statusCode + '>');
      }
      resolve(body);
    });
  });
}
