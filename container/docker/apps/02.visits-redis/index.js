const express = require("express")
const redis = require("redis")

const app = express()
const client = redis.createClient({
  host: "redis-server",
  port: 6379
})

client.set("visits", 0)

app.get("/", (req, res) => {
  
  //process.exit(0)   // Exit with status code 0: Exited and everything is OK
  //process.exit(1)   // Exit because something went wrong! 2, 3, 4 too
  client.get("visits", (err, visits) => {
    client.set("visits", parseInt(visits) + 1)
    res.send("Number of visits!! " + visits)
  })

})


app.listen(8081, () => {
  console.log("listening on port 8081");
});
