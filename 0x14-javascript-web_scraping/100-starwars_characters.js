#!/usr/bin/node

const request = require('request');
const myArgs = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films';

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
      if (info.results[i].episode_id === parseInt(myArgs[2])) {
        const characters = info.results[i].characters;
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
  }
}

request(options, callback);
