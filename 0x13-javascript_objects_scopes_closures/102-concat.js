#!/usr/bin/node

const fs = require('fs');
const myArgs = process.argv;

fs.readFile(myArgs[2], (err, data) => {
  if (err) {
    throw err;
  }
  fs.appendFile(myArgs[4], data, function (err) { if (err) throw err; });
});

fs.readFile(myArgs[3], (err, data) => {
  if (err) {
    throw err;
  }
  fs.appendFile(myArgs[4], data, function (err) { if (err) throw err; });
});
