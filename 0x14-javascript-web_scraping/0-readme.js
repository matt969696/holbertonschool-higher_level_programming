#!/usr/bin/node

const fs = require('fs');
const doc = process.argv[2];

fs.readFile(doc, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
