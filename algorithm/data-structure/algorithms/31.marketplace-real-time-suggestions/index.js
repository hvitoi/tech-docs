const repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"];
const customerQuery = "mouse";

// expected output for "mouse"
// res = [
//          ["mobile", "moneypot", "monitor"],
//          ["mouse", "mousepad"],
//          ["mouse", "mousepad"],
//          ["mouse", "mousepad"]
//        ]

const searchSuggestions = (repository, customerQuery) => {
  repository = repository.sort().map((el) => el.toLowerCase()); // O(n*log(n))

  const suggestions = [];
  // start iteration in customerQuery from  the second element
  for (let i = 1; i < customerQuery.length; i++) {
    const query = customerQuery.slice(0, i + 1).toLowerCase(); // get each individual query
    //const queryResult = repository.filter((keyword) => keyword.includes(query)); // get matching keywords for each query
    const queryResult = repository.filter((keyword) => {
      return query === keyword.slice(0, query.length);
    });
    suggestions.push(queryResult.slice(0, 3)); // get first 3 matches only
  }
  return suggestions;
};
console.log(searchSuggestions(repository, customerQuery));
