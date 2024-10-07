package main

import "io/ioutil"

filename := "file.txt"
data := "content to be saved"

ioutil.WriteFile(filename, []byte(data), 0666) // returns error (if the case)


// String text to be saved must be converted to array of bytes
