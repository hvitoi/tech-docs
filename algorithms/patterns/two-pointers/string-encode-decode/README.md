# String encoding & decoding

## Description

- Given an encoded string and the number of rows of the matrix used for encoding, return the decoded string.

- Example:
  - **input**: `"mnes__ya___mi"`
  - **output**: `"my name is"`
- Encoding matrix

```json
[
  ["m", "n", "e", "s", " "],
  [" ", "y", "a", " ", " "],
  [" ", " ", " ", "m", "i"]
]
```

## Solution steps

- **Decoding**

  1. First of all, check if the input parameters were passed (`encodedStr` and `numOfRows`). Also check if the number of rows is greater than zero.
  1. Determine the number of columns for the matrix.
  1. Populate the matrix sequentially with the letters of `encodedStr`.
  1. Once the matrix is populate, read the letters from the matrix in the correct order and join the letters.
  1. Trim the decoded string (remove trailing spaces, for example) and return the decoded result.

- **Encoding**

  1. Check if the input parameters were passed (`str` and `numOfRows`). Also checks if the number of rows is greater than zero.
  1. Determine the number of rows for the matrix.
  1. Initialize the matrix with empty values with the dimension `numOfRows`\*`numOfColumns`.
  1. Populate the matrix with the letters of the plain string in the correct order.
  1. Join the elements of the matrix in sequential order.
  1. Return the encoded string.

## Runtime complexity

- The runtime complexity for the `decodeString` method is based on the dimension of the encoding matrix.
- The dimension of the matrix can be calculated with the function `d = r*(n/r)`, where:
  - `n` is the length of the `encodedStr` input.
  - `r` is the integer `numOfRows` input.
- Simplifying the function `d = r*(n/r)` we get `d = n`.
- Therefore the runtime complexity is: `O(n)`.

## Tests

```shell
# install jest dependency
npm i

# run tests
npm run test
```
