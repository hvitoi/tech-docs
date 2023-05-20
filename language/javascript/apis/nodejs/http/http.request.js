const http = require("http");

const url =
  "http://api.weatherstack.com/current?access_key=6693daf76bb7789a5f54d89d22326243&query=34.592000,-106.3652";

// http.request(url, callback)
const request = http.request(url, (response) => {
  let data = "";

  response.on("data", (chunk) => {
    data = data + chunk.toString(); // Buffer needs to be converted to string
  });

  response.on("end", () => {
    body = JSON.parse(data);
    console.log(body);
  });
});

request.on("error", (error) => {
  console.log("An error", error);
});

request.end();
