// exporting by "foo.js"
function awesomeFunction() {
  console.log("hello!");
}
export { awesomeFunction };

// importing from "foo.js"
import { awesomeFunction } from "foo";
awesomeFunction(); // hello!
