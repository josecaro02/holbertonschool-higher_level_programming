#!/usr/bin/node
const myArg = process.argv;
if (parseInt(myArg[2])) {
  const szArg = parseInt(myArg[2]);
  for (let i = 0; i < szArg; i++) {
    console.log('X'.repeat(szArg));
  }
} else {
  console.log('Missing size');
}
