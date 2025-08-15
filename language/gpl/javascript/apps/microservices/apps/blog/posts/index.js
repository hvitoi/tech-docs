const express = require('express');
const { randomBytes } = require('crypto');
const bodyParser = require('body-parser');
const cors = require('cors');
const axios = require('axios');

// Create the API
const app = express();

// Configure the API
app.use(bodyParser.json()); // Parse body of requests
app.use(cors());

// Database of posts
const posts = {};

// Routes
app.post('/posts/create', async (req, res) => {
  const id = randomBytes(4).toString('hex');
  const { title } = req.body;

  // Add the new post into the database
  posts[id] = { id, title };

  // Emit the event of the post creation
  await axios.post('http://eventbus-clusterip:3000/events', {
    type: 'PostCreated',
    data: posts[id]
  });

  res.status(201).send(posts[id]);
});

app.post('/events', (req, res) => {
  res.send({});
});

// Listen
app.listen(3000, () => {
  console.log('Listening on port 3000.');
});
