#!/usr/bin/node
const nbArg = process.argv.length;
if (nbArg <= 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
