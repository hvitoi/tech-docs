# Mediator

- A middle man (middleware)
- Intercept every request and transforms it
- Eliminate code duplication

```typescript
import express from "express";
const app = express();

// Middleware logic
function mediator(req, res, next) {
  console.log("Request Type:", req.method);
  next();
}

app.use(mediator);

// Mediator runs before each route handler
app.get("/", (req, res) => {
  res.send("Hello World");
});

app.get("/about", (req, res) => {
  res.send("About");
});
```
