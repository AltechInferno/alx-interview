#!/usr/bin/node
const request = require('request');
const URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const characURL = JSON.parse(body).characters;
    const characName = characURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, characReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(characReqBody).name);
        });
      }));

    Promise.all(characName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
