const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

// ---

// API configuration
const app = express();
app.use(bodyParser.json());

// Events database
const events = [];

// Routes
app.post('/events', (req, res) => {
  const event = req.body;

  events.push(event); // Push the newest event to the database

  axios.post('http://posts-clusterip:3000/events', event); // posts
  axios.post('http://comments-clusterip:3000/events', event); // comments
  axios.post('http://query-clusterip:3000/events', event); // query
  axios.post('http://moderation-clusterip:3000/events', event); // moderation

  console.log(`Event received: ` + event.type);
  res.send({ status: 'OK' });
});

app.get('/events', (req, res) => {
  res.send(events);
});

// Listen
app.listen(3000, () => {
  console.log('Listening on port 3000.');
});
