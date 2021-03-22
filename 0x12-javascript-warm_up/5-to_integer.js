#!/usr/bin/node
const myArg = parseInt(process.argv[2], 10);
if (isNaN(myArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myArg);
}
