# Fleet Combinations

## Description

- Find the possible number of combinations of 2-wheel and 4-wheels vehicles for a given number of total wheels.
- Example:
  - **input**: `[4, 5, 6]`
  - **output**: `[2, 0, 2]`

## Solution steps

1. Iterate over the input array `wheels` containing the total number of wheels for each case.
   1. On each iteration over the array, check if the element is dividable by 2. If it is not, returns 0 for that element in the array.
   1. If the element is dividable by 2, calculate the total number of possible combinations with the function `Math.floor(wheel/4) + 1` and return it.
1. Return the array with the possible fleet combination for each analyzed number of wheels.

## Runtime complexity

- The runtime complexity of the algorithm is based on the size of the input array `wheels`.
- The runtime complexity increases **linearly** as the size (`n`) of input increases.
- Therefore, the runtime complexity is: `O(n)`.

## Tests

```shell
# install jest dependency
npm i

# run tests
npm run test
```
