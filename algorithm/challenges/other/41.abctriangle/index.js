const abcTriangle = (letter) => {
  // validar se letter está entre a-z (usar regex)
  if (!letter.match(/[a-z]/)) console.log("deve estar entre a-z");

  // calcular n: quantidade total de letras a serem impressas, a -> 1, b->2, z->26 ...
  const n = letter.charCodeAt(0) - "a".charCodeAt(0) + 1;

  // percorre de i=1 ate n
  // for (let i = 0; i < n; i++) {
  //   // definir a letter atual
  //   const currentLetter = String.fromCharCode("a".charCodeAt(0) + i);

  //   // imprime a letra atual i vezes (qteTotal)
  //   console.log(currentLetter.repeat(i + 1));
  // }

  const arr = Array.from({ length: n }, (_, i) =>
    String.fromCharCode("a".charCodeAt(0) + i)
  );
  arr.forEach((l, i) => console.log(l.repeat(i + 1)));
};

abcTriangle("e");
