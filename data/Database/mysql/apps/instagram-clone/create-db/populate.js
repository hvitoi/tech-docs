const faker = require('faker');
const mysql = require('mysql');

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '123',
  database: 'join_us',
});

connection.connect();
let q;

// INSERT classic
q = `INSERT INTO user (name, email) VALUES ('Rusty', 'rusty@email.com')`;
connection.query(q, (err, res, fields) => {
  if (err) throw err;
  console.log(res);
});

// INSERT object
const person = {
  name: faker.name.firstName(),
  email: faker.internet.email(),
  created_at: faker.date.past(),
};
let end_result = connection.query(
  'INSERT INTO user SET ?',
  person,
  (err, result) => {
    if (err) throw err;
    console.log(result);
  }
);
console.log(end_result.sql); // shows the compiled sql that was sent

// INSERT multiple
var data = [];
for (var i = 0; i < 500; i++) {
  data.push([
    faker.name.firstName(),
    faker.internet.email(),
    faker.date.past(),
  ]);
}
q = 'INSERT INTO user (name, email, created_at) VALUES ?';
connection.query(q, [data], (err, res) => {
  console.log(err);
  console.log(res);
});

// SELECT
q = 'SELECT * FROM user';
connection.query(q, (err, res, fields) => {
  if (err) throw err;
  console.log(res);
});

connection.end();
