#!/usr/bin/node

const request = require('request');
const myArgs = process.argv;
const url = myArgs[2];
let count = 0;

const options = {
  url: url,
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    for (let i = 0; i < info.count; i++) {
      const characters = info.results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('190') > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
}
request(options, callback);
