#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

const options = {
  url: url,
  headers: {
    'User-Agent': 'request'
  }
};

function callback (error, response, body) {
  if (!error && response.statusCode === 200) {
    const dict = {};
    const info = JSON.parse(body);
    for (let i = 0; i < info.length; i++) {
      const userID = info[i].userId;
      if (dict[userID]) {
        if (info[i].completed === true) {
          dict[userID]++;
        }
      } else {
        if (info[i].completed === true) {
          dict[userID] = 1;
        }
      }
    }
    console.log(dict);
  }
}
request(options, callback);
