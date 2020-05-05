#!/usr/bin/node
const myArg = process.argv;
if (parseInt(myArg[2]) && parseInt(myArg[2]) >= 0) {
  for (let i = 0; i < parseInt(myArg[2]); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
