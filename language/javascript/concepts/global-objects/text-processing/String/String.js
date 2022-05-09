// STRINGS
var texto = 'Este eh um texto com "texto" dentro.';
var outroTexto = 'Este eh um texto com "texto" dentro.';
console.log(texto);
console.log(outroTexto);
// CODE OUTPUT: \' single quote \" double quote \\ backslash \n newline \r carriage return \t tab \b backspace \f form feed
var novoTexto = texto + outroTexto;
console.log(novoTexto);

console.log(novoTexto[0]); // First letter
console.log(novoTexto.length); // String size
console.log(novoTexto[novoTexto.length - 1]); // Last letter

var novoTexto = "Hello World";
//try { var novoTexto[0] = 'J'; } catch (e) { } // Cannot change single character
console.log(novoTexto);

// MULTI LINE String
var person = {
  name: "Henrique",
  age: 25,
};
var greeting = `Hello, my name is ${person.name}!
I am ${person.age} years old.`;
console.log(greeting);
