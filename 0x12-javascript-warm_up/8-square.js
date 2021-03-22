#!/usr/bin/node
const myArg = parseInt(process.argv[2], 10);
if (isNaN(myArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myArg; i++) {
    console.log('X'.repeat(myArg));
  }
}
