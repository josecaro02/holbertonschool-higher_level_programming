#!/usr/bin/node

const request = require('request');
const myArgs = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + myArgs[2];
const orderDict = {};
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
          saveNames(name.split('/')[5], resultName.name, characters.length);
        }
      });
    }
  }
}

function saveNames (id, value, size) {
  orderDict[id] = value;
  if (Object.entries(orderDict).length === size) {
    for (const key in orderDict) {
      console.log(orderDict[key]);
    }
  }
}
request(options, callback);
