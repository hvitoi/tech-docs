const sgMail = require("@sendgrid/mail");

sgMail.setApiKey("my-api-key");

const msg = {
  to: "hav_gt@yahoo.com.br",
  from: "hvitoi@gmail.com",
  subject: "Sending with Twilio SendGrid is Fun",
  text: "and easy to do anywhere, even with Node.js",
  html: "<strong>and easy to do anywhere, even with Node.js</strong>",
};

sgMail.send(msg);
