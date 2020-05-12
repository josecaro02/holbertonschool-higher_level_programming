#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (newDict[value]) {
    newDict[value].push(key);
  } else {
    newDict[value] = [];
    newDict[value].push(key);
  }
}
console.log(newDict);
