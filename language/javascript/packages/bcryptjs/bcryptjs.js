const bcrypt = require("bcryptjs");

const doEncryptIt = async (password) => {
  const hashedPassword = await bcrypt.hash(password, 8); // 8 rounds of encryption
  const isPasswordCorrect = await bcrypt.compare("oi12345", hashedPassword);
  return isPasswordCorrect;
};

doEncryptIt("oi12345");
