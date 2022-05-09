const WebSocket = require("ws");

const server = new WebSocket.Server({ port: "8080" });
server.on("connection", (socket) => {
  // handle incoming messages
  socket.on("message", (message) => {
    // send a message back to client
    socket.send(`roger that! ${message}`);
  });
});
