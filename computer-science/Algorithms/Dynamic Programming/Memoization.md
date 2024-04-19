# Memoization

- An optimization technique that uses `cache`
- Ideally memoization uses `clojures` (a function that returns a function)
  - This way, it's possible to define the cache in the context of the outer function and `avoid a global cache`
  - With that, `the cache is embedded in the memoized function definition`
- Memoization increases the `space complexity` by the size of the cache store, usually $O(n)$
