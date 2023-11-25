// Create elements
const h1Element = document.createElement("h1");
const h2Element = document.createElement("h2");

// Append the content of h2 into h2
h1Element.append(h2Element.content); // content is of type DocumentFragment
