#!/usr/bin/node

const fs = require('fs');
const myArgs = process.argv;

fs.appendFile(myArgs[2], myArgs[3], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
