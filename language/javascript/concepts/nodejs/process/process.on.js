// Interrupt
process.on("SIGINT", () => console.log("Closing"));

// Terminate
process.on("SIGTERM", () => console.log("Closing"));

// Exception
process.on("uncaughtException", () => console.log("Exception"));
