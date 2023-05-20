var myVar = "Henrique"; // global variable
let myLet = "Vitoi"; // block variable
const myConst = 3.14; // block variable (immutable)

function checkScopeVar() {
  var scope = "Function Scope";
  if (true) {
    var scope = "Block Scope"; // completely override the first declaration
    console.log(scope);
  }
  console.log(scope);
}
checkScopeVar();

function checkScopeLet() {
  let scope = "Function Scope";
  if (true) {
    let scope = "Block Scope"; // keep the outter scope variable
    console.log(scope);
  }
  console.log(scope);
}
checkScopeLet();

function checkScopeConst() {
  const scope = "Function Scope";
  if (true) {
    const scope = "Block Scope"; // keep the outter scope variable
    console.log(scope);
  }
  console.log(scope);
}
checkScopeConst();
