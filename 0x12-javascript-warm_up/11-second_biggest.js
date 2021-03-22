#!/usr/bin/node
const myArr = process.argv.slice(2);
if (myArr.length <= 1) {
  console.log(0);
} else {
  const myNb = myArr.map(i => Number(i)).sort(function (a, b) { return b - a; })[1];
  console.log(myNb);
}
