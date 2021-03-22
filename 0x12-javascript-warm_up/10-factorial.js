#!/usr/bin/node
function fact (n) {
  const myN = parseInt(n, 10);
  if (isNaN(myN)) {
    return 1;
  } else if (myN <= 1) {
    return 1;
  } else {
    return myN * fact(myN - 1);
  }
}
console.log(fact(process.argv[2]));
