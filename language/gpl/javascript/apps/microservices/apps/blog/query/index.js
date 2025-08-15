const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const axios = require('axios');

// ---

// API configuration
const app = express();
app.use(bodyParser.json());
app.use(cors());

// Database: Data structure containing the posts with comments inside
const posts = {};

// Possible events received
const handleEvent = (type, data) => {
  if (type === 'PostCreated') {
    const { id, title } = data;
    posts[id] = { id, title, comments: [] };
  }

  if (type === 'CommentCreated') {
    const { id, content, postId, status } = data;
    posts[postId].comments.push({ id, content, status });
  }

  if (type === 'CommentUpdated') {
    const { id, content, postId, status } = data;
    const post = posts[postId];
    const comment = post.comments.find((comment) => comment.id === id);
    comment.status = status;
    comment.content = content;
  }
};

// Routes
app.get('/posts', (req, res) => {
  res.send(posts);
});

app.post('/events', (req, res) => {
  const { type, data } = req.body;
  handleEvent(type, data);

  res.send({});
});

// Listen
app.listen(3000, async () => {
  console.log('Listening on port 3000.');

  // Get all events stored in the event bus
  const res = await axios.get('http://eventbus-clusterip:3000/events');

  // Handle all events
  for (let event of res.data) {
    console.log('Processing event:', event.type);
    handleEvent(event.type, event.data);
  }
});
