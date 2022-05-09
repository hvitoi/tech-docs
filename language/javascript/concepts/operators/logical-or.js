const obj = { duration: 50, title: "" };

// only assigns if left-hand statement is falsy
// assign only if it's not already defined
obj.duration ||= 10;
obj.title ||= "title is empty.";

console.log(obj);
