const sgMail = require("@sendgrid/mail");

sgMail.setApiKey("my-api-key");

const msg = {
  to: "user2@example.com",
  from: "user1@example.com",
  subject: "Sending with Twilio SendGrid is Fun",
  text: "and easy to do anywhere, even with Node.js",
  html: "<strong>and easy to do anywhere, even with Node.js</strong>",
};

sgMail.send(msg);
