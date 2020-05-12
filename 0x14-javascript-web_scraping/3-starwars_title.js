#!/usr/bin/node

const request = require('request');
const myArgs = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[2];

const options = {
  url: url,
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    console.log(info.title);
  }
}

request(options, callback);
