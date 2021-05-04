#!/usr/bin/node
/* Task 1 */

const fs = require('fs');
const doc = process.argv[2];
const text = process.argv[3];

fs.writeFile(doc, text, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
