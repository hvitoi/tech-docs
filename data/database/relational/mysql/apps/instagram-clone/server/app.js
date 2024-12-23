// Modules
const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

// Initialize express
const app = express();

// Express config
app.set('view engine', 'ejs'); // in /views directory by default
app.use(bodyParser.urlencoded({ extended: true })); // Automatically parse .json from request (req)
app.use(express.static(__dirname + '/public')); // Directory for .css and other assets

// MySQL connection
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '123',
  database: 'join_us',
});

// Route (get)
app.get('/', (req, res) => {
  // Count users
  connection.query('SELECT COUNT(*) AS count FROM user', (err, results) => {
    if (err) throw err;
    res.render('home', { count: results[0].count });
  });
});

// Route (post)
app.post('/register', (req, res) => {
  const person = {
    name: req.body.name,
    email: req.body.email,
  };
  connection.query('INSERT INTO user SET ?', person, (err, result) => {
    if (err) throw err;
    res.redirect('/'); // Redirect
  });
});

// Listen
app.listen(3000, () => {
  console.log('Server running on port 3000.');
});
