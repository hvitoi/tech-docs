# IO bound vs. CPU bound

## I/O bound

- Normally refers to "I/O operations" (I/O bound operations) that are relatively slow (compared to the speed of the processor and the RAM memory):
  - the data from the client to be sent through the network
  - the data sent by your program to be received by the client through the network
  - the contents of a file in the disk to be read by the system and given to your program
  - the contents your program gave to the system to be written to disk
  - a remote API operation
  - a database operation to finish
  - a database query to return the results

## CPU bound

- Audio or image processing.
- `Computer vision`: an image is composed of millions of pixels, each pixel has 3 values / colors, processing that normally requires computing something on those pixels, all at the same time.
- `Machine Learning`: it normally requires lots of "matrix" and "vector" multiplications. Think of a huge spreadsheet with numbers and multiplying all of them together at the same time.
- `Deep Learning`: this is a sub-field of Machine Learning, so, the same applies. It's just that there is not a single spreadsheet of numbers to multiply, but a huge set of them, and in many cases, you use a special processor to build and / or use those models.
