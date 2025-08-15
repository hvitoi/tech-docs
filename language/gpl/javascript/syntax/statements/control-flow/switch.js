const expr = "Papayas";

switch (expr) {
  case "Oranges":
    console.log("Oranges are $0.59 a pound.");
    break;
  case "Mangoes":
  case "Papayas":
    console.log("Mangoes and papayas are $2.79 a pound.");
    // expected output: "Mangoes and papayas are $2.79 a pound."
    break;
  default:
    console.log(`Sorry, we are out of ${expr}.`);
}

var val = 2;
switch (val) {
  case 1:
    console.log("alpha");
    break;
  case 2:
    console.log("beta");
    break;
  case 3:
    console.log("gamma");
    break;
  default:
    console.log("none of the above");
}
switch ("bob") {
  case 1:
  case 2:
  case 3:
    console.log("Low");
    break;
  case 4:
  case "bob":
  case 6:
    console.log("Mid");
    break;
  case 7:
  case 8:
  case 9:
    console.log("High");
    break;
}
