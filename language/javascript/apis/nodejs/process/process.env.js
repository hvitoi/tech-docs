// Check if a environment variable exists
if (!process.env.JWT_KEY) {
  throw new Error("JWT_KEY must be defined");
}
