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
    const characters = info.characters;
    for (let k = 0; k < characters.length; k++) {
      const name = characters[k];
      request(name, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          const resultName = JSON.parse(body);
          console.log(resultName.name);
        }
      });
    }
  }
}

request(options, callback);
