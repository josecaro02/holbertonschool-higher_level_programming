#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const myArgs = process.argv;
const url = myArgs[2];

const options = {
  url: url,
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = body;
    fs.appendFile(myArgs[3], info, 'utf8', (err, data) => {
      if (err) {
        console.log(err);
      }
    });
  }
}
request(options, callback);
