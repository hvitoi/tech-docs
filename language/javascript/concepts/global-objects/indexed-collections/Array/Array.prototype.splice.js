// O(N)

var myFish = ["angel", "clown", "mandarin", "surgeon"];
console.log(myFish);

var removed = myFish.splice(2, 0, "drum");
console.log("Remove 0 elementos a partir do índice 2, e insere 'drum'");
console.log(removed); // [] (nenhum elemento removido)
console.log(myFish); // ["angel", "clown", "drum", "mandarin", "surgeon"]

removed = myFish.splice(3, 1);
console.log("Remove 1 elemento do índice 3");
console.log(removed); //["mandarim"]
console.log(myFish); // ["angel", "clown", "drum", "surgeon"]

removed = myFish.splice(2, 1, "trumpet");
console.log("Remove 1 elemento a partir do índice 2, e insere 'trumpet'");
console.log(removed); // ["drum"]
console.log(myFish); // ["angel", "clown", "trumpet", "surgeon"]

removed = myFish.splice(0, 2, "parrot", "anemone", "blue");
console.log(
  "Remove 2 elementos a partir do índice 0, e insere 'parrot', 'anemone' e 'blue'"
);
console.log(removed); // ["angel", "clown"]
console.log(myFish); // ["parrot", "anemone", "blue", "trumpet", "surgeon"]

removed = myFish.splice(3, Number.MAX_VALUE);
console.log("Remove todos elementos a partir do indice 3");
console.log(removed); // ["trumpet", "surgeon"]
console.log(myFish); // ["parrot", "anemone", "blue"]
