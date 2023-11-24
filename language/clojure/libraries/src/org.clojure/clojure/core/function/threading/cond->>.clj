(cond->> {:a 1 :b 2}
  true vals
  false (map inc)
  true (reduce +))
