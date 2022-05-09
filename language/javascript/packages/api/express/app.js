const path = require("path");
const express = require("express");
const expressWs = require("express-ws");

const app = express();
expressWs(app);

// REST endpoint
app.get("/api", (req, res) => {
  console.log("API was called!");
  // res.status(200).send("Hello World");
  res.status(200).json({ msg: "Success!" });
});

// HTML endpoint
app.get("/page", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

// Web socket endpoint (full-duplex)
app.ws("/echo", (ws, req) => {
  ws.on("message", (msg) => {
    ws.send(msg);
  });
});

app.listen(3000);
