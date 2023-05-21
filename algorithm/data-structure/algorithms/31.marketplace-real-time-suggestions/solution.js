

const suggestions = (repository, searchQuery) => {
  repository = repository.sort().map((el) => el.toLowerCase()); // O(n*log(n))
  searchQuery = searchQuery.toLowerCase();

  const suggestions = [];

  for (let len = 2; len <= searchQuery.length; len++) {
    //const queryResult = repository.filter((keyword) => keyword.includes(query)); // get matching keywords for each query
    const searchResults = repository
      .filter((keyword) => keyword.slice(0, len) === searchQuery.slice(0, len))
      .slice(0, 3); // 3 first results
    suggestions.push(searchResults);
  }

  return suggestions;
};




// --

const repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"];
const searchQuery = "mouse";

// expected output for "mouse"
// res = [
//          ["mobile", "moneypot", "monitor"],
//          ["mouse", "mousepad"],
//          ["mouse", "mousepad"],
//          ["mouse", "mousepad"]
//        ]

console.log(suggestions(repository, searchQuery));
