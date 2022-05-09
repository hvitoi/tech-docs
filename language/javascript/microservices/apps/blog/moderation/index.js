const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

// ---

// API configuration
const app = express();
app.use(bodyParser.json());

// Routes
app.post('/events', async (req, res) => {
  const { type, data } = req.body;

  if (type === 'CommentCreated') {
    const status = data.content.includes('orange') ? 'rejected' : 'approved';
    await axios.post('http://eventbus-clusterip:3000/events', {
      type: 'CommentModerated',
      data: { ...data, status }
    });
  }
  res.send({});
});

// Listen
app.listen(3000, () => {
  console.log('Listening on port 3000.');
});
