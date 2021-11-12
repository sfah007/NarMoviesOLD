const fetch = require("node-fetch")

function getvals(){
  return fetch('https://httpbin.org/headers',
  {
    method: "GET",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    },
  })
  .then((response) => response.json())
  .catch(error => console.warn(error));
}

function getvals2(){
  return fetch('https://httpbin.org/get',
  {
    method: "GET",
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    },
  })
  .then((response) => response.json())
  .catch(error => console.warn(error));
}

getvals().then(response => getvals2().then(response2 => console.log({"1" : response , "2" : response2})));
