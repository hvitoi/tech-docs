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

// Comments Database
const commentsByPost = {};

// Routes
app.get('/posts/:id/comments', (req, res) => {
  res.send(commentsByPost[req.params.id] || []);
});

app.post('/posts/:id/comments', async (req, res) => {
  const commentId = randomBytes(4).toString('hex');
  const postId = req.params.id;
  const { content } = req.body;

  const newComment = { id: commentId, content, status: 'pending' };
  if (commentsByPost[postId]) commentsByPost[postId].push(newComment);
  else commentsByPost[postId] = [newComment];

  // Emit the event of the post creation
  await axios.post('http://eventbus-clusterip:3000/events', {
    type: 'CommentCreated',
    data: { ...newComment, postId }
  });

  res.status(201).send(commentsByPost[postId]);
});

app.post('/events', async (req, res) => {
  const { type, data } = req.body;

  if (type === 'CommentModerated') {
    const { postId, id, status } = data;
    const comments = commentsByPost[postId];

    const comment = comments.find((comment) => comment.id === id);
    comment.status = status; // Object here is the same in memory

    await axios.post('http://eventbus-clusterip:3000/events', {
      type: 'CommentUpdated',
      data: { ...comment, postId }
    });
  }
  res.send({});
});

// Listen
app.listen(3000, () => {
  console.log('Listening on port 3000.');
});
