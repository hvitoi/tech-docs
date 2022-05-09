const jwt = require("jsonwebtoken");

const myFunction = async () => {
  // sign() returns the authentication token: sign(data, signature, options)
  // token: header.payload(body).signature
  const token = jwt.sign({ _id: "abc123" }, "secret", {
    expiresIn: "7 seconds",
  });
  console.log(token);

  // verify() returns the payload of the token if the signature is correct
  const data = jwt.verify(token, "secret");
  console.log(data);
};
myFunction();
