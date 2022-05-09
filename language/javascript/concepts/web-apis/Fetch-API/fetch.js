fetch("http://example.com/movies.json")
  .then((response) => response.json())
  .then((data) => console.log(data));

await fetch("http://example.com/movies.json", {
  method: "POST", // *GET, POST, PUT, DELETE, etc.
  mode: "cors", // no-cors, *cors, same-origin
  cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
  credentials: "same-origin", // include, *same-origin, omit
  headers: {
    "Content-Type": "application/json",
    // 'Content-Type': 'application/x-www-form-urlencoded',
  },
  redirect: "follow", // manual, *follow, error
  referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
  body: JSON.stringify({ a: "b" }), // body data type must match "Content-Type" header
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((err) => console.error(err));
