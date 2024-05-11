const { encodeString } = require("./app");
const { decodeString } = require("./app");

describe("decode string", () => {
  test("function is defined", () => {
    expect(decodeString).toBeDefined();
  });

  test("correctly decodes an encoded string with n=3", () => {
    expect(decodeString("mnes__ya_____mi", 3)).toEqual("my name is");
  });

  test("correctly decodes an encoded string with n=6", () => {
    expect(decodeString("me_____y_______i_____ns_____a______m", 6)).toEqual(
      "my name is"
    );
  });
});

describe("encode string", () => {
  test("encodeString function is defined", () => {
    expect(encodeString).toBeDefined();
  });

  test("decodeString correctly decodes an encoded string with n=3", () => {
    expect(encodeString("my name is", 3)).toEqual("mnes__ya_____mi");
  });

  test("decodeString correctly decodes an encoded string with n=6", () => {
    expect(encodeString("my name is", 6)).toEqual(
      "me_____y_______i_____ns_____a______m"
    );
  });
});
