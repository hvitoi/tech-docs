// Destructuring mongodb module
const { MongoClient, ObjectID } = require("mongodb");

// Connection info
const connectionURL = "mongodb://127.0.0.1:27017";
const databaseName = "task-manager";

// MongoClient.connect(url, {options}, callback(e,c))
MongoClient.connect(
  connectionURL,
  { useNewUrlParser: true, useUnifiedTopology: true },
  (err, client) => {
    if (err) {
      return console.log("Failed to connect to the database");
    }
    // Connect to the db
    const db = client.db(databaseName);

    // CRUD
    // C - insertOne / insertMany
    // R - findOne / find
    // U - updateOne
    // D -

    // CREATE
    db.collection("users").insertOne({
      name: "Joao",
      age: 26,
    });

    db.collection("users").insertOne(
      {
        name: "Henrique",
        age: 26,
      },
      (err, result) => {
        if (err) {
          return console.log("Unable to insert user");
        }
        // result.ops is the document inserted
        console.log(result.ops);
      }
    );

    db.collection("tasks").insertMany(
      [
        {
          description: "Clean the house",
          completed: true,
        },
        {
          description: "Renew inspection",
          completed: true,
        },
        {
          description: "Pot plants",
          completed: false,
        },
      ],
      (err, result) => {
        if (err) {
          return console.log("Unable to many documents");
        }
        console.log(result.ops);
      }
    );

    // READ
    db.collection("users").findOne({ name: "Henrique" }, (err, data) => {
      if (err) {
        return console.log("Unable to fetch");
      }
      console.log(data);
    });

    db.collection("users").findOne({ age: 1 }, (err, data) => {
      if (err) {
        return console.log("Unable to fetch");
      }

      console.log(data);
    });

    db.collection("users").findOne(
      { _id: new ObjectID("5ea48e26aff7523451f52011") },
      (err, data) => {
        if (err) {
          return console.log("Unable to fetch");
        }

        console.log(data);
      }
    );

    db.collection("users")
      .find({ age: 26 })
      .toArray((err, data) => {
        // To array return the matching search
        console.log(data);
      });

    db.collection("users")
      .find({ age: 26 })
      .count((err, data) => {
        // Count search results
        console.log(data);
      });

    db.collection("tasks").findOne(
      { _id: new ObjectID("5ea48e26aff7523451f52011") },
      (err, data) => {
        if (err) {
          return console.log("Unable to fetch");
        }

        console.log(data);
      }
    );

    db.collection("tasks")
      .find({ completed: false })
      .toArray((err, data) => {
        // Count search results
        if (err) {
          return console.log("Unable to fetch");
        }
        console.log(data);
      });

    // UPDATE
    db.collection("users")
      .updateOne(
        {
          _id: new ObjectID("5ea46d7e2a5b691ca3bb2f55"), //filter
        },
        {
          $set: {
            // "$set" is the operator to set new values
            name: "Mike", // Other properties remain unchanged
          }, // $unset to remove, $rename, $inc (increment)... etc
          $inc: {
            age: 1, // From 26 to 27
          },
        }
      )
      .then((res) => {
        console.log(res); // res.modifiedCount returns 0 or 1
      })
      .catch((err) => {
        console.log(err);
      });

    db.collection("tasks")
      .updateMany(
        {
          completed: false,
        },
        {
          $set: {
            completed: true,
          },
        }
      )
      .then((res) => {
        console.log(res.modifiedCount);
      })
      .catch((err) => {
        console.log(err);
      });

    // DELETE
    db.collection("users")
      .deleteOne({
        age: 20,
      })
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });

    db.collection("users")
      .deleteMany({
        age: 20,
      })
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  }
);
