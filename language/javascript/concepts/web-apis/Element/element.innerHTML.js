// (Element).querySelector: HTMLInputElement | null
// query can be .class, #id, or 'elementName'

// Get a element
const selectedElement = document.body.querySelector("h1");
const selectedElement2 = document.body.querySelector("lhqawf"); // Get back 'null'

console.log(selectedElement);

// Extract the text of the element
const text = selectedElement.innerHTML;

console.log(text);

// ---

// Create element
const h2Element = document.createElement("h2");

// Access the innerHtml
h2Element.innerHTML = "Hehehe";
console.log(h2Element);
