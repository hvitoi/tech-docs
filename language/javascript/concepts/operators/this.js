const john = {
  face: "🥰",
  whodis() {
    console.log(this);
  },
  butWhoAmI: () => {
    console.log(this);
  },
};

john.whodis(); // "this" is the left hand object (john)
john.butWhoAmI(); // "this" is based on the enclosing object (global this)

// ---

function Horse(name) {
  this.name = name;
  this.sayHello = function () {
    console.log(this.name);
  };
}
const myHorse = new Horse("Secretariat");
myHorse.sayHello();
