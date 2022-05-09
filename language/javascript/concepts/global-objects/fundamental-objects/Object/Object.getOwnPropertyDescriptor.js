// Get the configuration object about a object key

const myself = { name: "henry", age: 27 };
const myselfInfo = Object.getOwnPropertyDescriptor(myself, "name");
console.log(myselfInfo);

/**
 * value
 * writable
 * enumerable
 * configurable
 */
