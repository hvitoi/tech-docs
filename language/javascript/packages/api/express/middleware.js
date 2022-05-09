// Authentication Middleware
app.use((req, res, next) => {
  // req and res are exactly the same information given to the routers handlers
  if (req.method === "GET") {
    // req.method: http request used (get, post...)
    res.send("GET requests are disabled");
  } else {
    next(); //next() ends the middleware and run the conventional router handler
  }
});

// Maintenance middleware
app.use((req, res, next) => {
  res.status("503").send("Service temporarely unavailable");
});
