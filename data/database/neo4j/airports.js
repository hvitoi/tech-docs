const airports = [
  "PHX",
  "BKK",
  "OKC",
  "JFK",
  "LAX",
  "MEX",
  "EZE",
  "HEL",
  "LOS",
  "LAP",
  "LIM",
];

const routes = [
  ["PHX", "LAX"],
  ["PHX", "JFK"],
  ["JFK", "OKC"],
  ["JFK", "HEL"],
  ["JFK", "LOS"],
  ["MEX", "LAX"],
  ["MEX", "BKK"],
  ["MEX", "LIM"],
  ["MEX", "EZE"],
  ["LIM", "BKK"],
];

/**
 * Adjacency List
 */
const adjacencyList = new Map();

airports.forEach((airport) => {
  adjacencyList.set(airport, new Set()); // add nodes with 0 edges
});

routes.forEach(([origin, destination]) => {
  adjacencyList.get(origin).add(destination); // add edge bidirectional
  adjacencyList.get(destination).add(origin); // add edge bidirectional
});

console.log(adjacencyList);

/**
 * DFS
 */
const dfsRecursive = (
  currentAirport,
  finalDestination,
  visitedAirports = new Set()
) => {
  // mark the current airport as visited
  visitedAirports.add(currentAirport);
  console.log(currentAirport);

  // get all next airports
  const nextAirports = adjacencyList.get(currentAirport);

  // return if the final destination is reached
  if (nextAirports.has(finalDestination)) return true; // base case

  // recurse if the final destination is not yet reached
  for (let nextAirport of nextAirports) {
    if (visitedAirports.has(nextAirport)) continue;
    if (dfs(nextAirport, finalDestination, visitedAirports)) return true;
  }

  return false;
};

/**
 * BFS
 */
const bfs = (origin, destination) => {
  const nodes = [origin];
  const visitedAirports = new Set();
  while (nodes.length) {
    // extract node
    const node = nodes.shift();

    // mark node at visited
    visitedAirports.add(node);

    // print node
    node === destination ? console.log(node + ": found!") : console.log(node);

    // push children to be processed
    const nodeChildrenFiltered = [...adjacencyList.get(node)].filter(
      (nodeChild) => !visitedAirports.has(nodeChild)
    );
    nodes.push(...nodeChildrenFiltered);
  }
};

/**
 * DFS
 */
const dfs = (origin, destination) => {
  const nodes = [origin];
  const visitedAirports = new Set();
  while (nodes.length) {
    // extract node
    const node = nodes.pop();

    // mark node at visited
    visitedAirports.add(node);

    // print node
    node === destination ? console.log(node + ": found!") : console.log(node);

    // push children to be processed
    const nodeChildrenFiltered = [...adjacencyList.get(node)].filter(
      (nodeChild) => !visitedAirports.has(nodeChild)
    );
    nodes.push(...nodeChildrenFiltered);
  }
};

// console.log(dfs("PHX", "BKK"));
// bfs("PHX", "BKK");
dfs("PHX", "BKK");
