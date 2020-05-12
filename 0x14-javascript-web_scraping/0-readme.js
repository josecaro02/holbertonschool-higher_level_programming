#!/usr/bin/node

const fs = require('fs');
const myArgs = process.argv;

fs.readFile(myArgs[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
