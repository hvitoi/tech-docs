// O(N)

const players = [
  {
    name: "Henrique",
    points: 100,
    xp: 10,
  },
  {
    name: "Marcio",
    points: 70,
    xp: 5,
  },
  {
    name: "Rich",
    points: 130,
    xp: 5,
  },
];

// ---

// Do operations in a object
const totalPoints = players.reduce((sum, element) => {
  return sum + element.points;
}, 0); // 0 is the initial 'sum' value
console.log(totalPoints);

// ---

const totalStats = players.reduce(
  (sum, element) => {
    // sum refers to the object below!
    sum.points += element.points;
    sum.xp += element.xp;
    return sum;
  },
  {
    // Initial 'sum' object value
    points: 0,
    xp: 0,
  }
);

console.log(totalStats);

// ---

annotatedMethods = ["leads", "leads", "leads2"];

// Find the unique topics subscribed to
const uniqueTopics = annotatedMethods.reduce((uniqueTopics, element) => {
  uniqueTopics.includes(element.meta) ? null : uniqueTopics.push(element.meta);
  return uniqueTopics;
}, []);
console.log(uniqueTopics);

// ---
// Sum 2 numbers
const data = ["2", "3", "5"];
const sum = (data || []).reduce((sum, el) => Number(sum) + Number(el));
const sum = (data || []).reduce((sum, number) => sum + number);
console.log(sum);
