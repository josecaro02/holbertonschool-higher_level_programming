#!/usr/bin/node

const request = require('request');
const myArgs = process.argv;
const url = myArgs[2];

request.get(url)
  .on('response', function (response) {
    console.log('code: ' + response.statusCode);
  });
