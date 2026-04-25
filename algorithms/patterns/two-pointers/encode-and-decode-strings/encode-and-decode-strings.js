const decodeString = (encodedStr, numOfRows) => {
  if (!encodedStr || !numOfRows || numOfRows <= 0) return null;

  // determine the number of columns for the matrix
  const numOfColumns = encodedStr.length / numOfRows;

  // populate matrix
  const arr = [];
  let index = 0;
  for (let r = 0; r < numOfRows; r++) {
    if (!arr[r]) arr[r] = [];
    for (let c = 0; c < numOfColumns; c++) {
      if (encodedStr[index] === "_") {
        arr[r][c] = " ";
      } else {
        arr[r][c] = encodedStr[index];
      }
      index++;
    }
  }
  // console.log(arr);

  // read matrix and build the decoded string
  let decodedString = "";
  let row = 0;
  let column = 0;
  while (arr[row][column]) {
    decodedString += arr[row][column];

    // move 2D index
    column = row === numOfRows - 1 ? column - numOfRows + 2 : column + 1;
    row = row === numOfRows - 1 ? 0 : row + 1;
  }

  // return decoded string (removing trailing spaces)
  return decodedString.trim();
};

const encodeString = (str, numOfRows) => {
  if (!str || !numOfRows || numOfRows <= 0) return null;

  // determine the number of columns for the matrix
  let numOfColumns = 0;
  if (str.length <= numOfRows) {
    numOfColumns = str.length;
  } else {
    numOfColumns = Math.floor(str.length / numOfRows) + numOfRows - 1;
  }

  // initialize empty matrix
  const arr = [];
  for (let r = 0; r < numOfRows; r++) {
    if (!arr[r]) arr[r] = [];
    for (let c = 0; c < numOfColumns; c++) {
      arr[r][c] = " ";
    }
  }

  // populate matrix
  let row = 0;
  let column = 0;
  for (let i = 0; i < str.length; i++) {
    arr[row][column] = str[i];

    // move 2D index
    column = row === numOfRows - 1 ? column - numOfRows + 2 : column + 1;
    row = row === numOfRows - 1 ? 0 : row + 1;
  }
  // console.log(arr);

  // join matrix elements in sequential order
  let encodedString = "";
  for (let r = 0; r < numOfRows; r++) {
    for (let c = 0; c < numOfColumns; c++) {
      if (arr[r][c] === " " || arr[r][c] === "") {
        arr[r][c] = "_";
      }
      encodedString += arr[r][c];
    }
  }

  // return encoded string
  return encodedString;
};

// const encoded = encodeString();
// const decoded = decodeString(encoded, 6);
// console.log(encoded);
// console.log(decoded);

module.exports = { encodeString, decodeString };
