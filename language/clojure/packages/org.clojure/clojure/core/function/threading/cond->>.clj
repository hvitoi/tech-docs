(->> my-map
     true vals
     false (map inc)
     true (reduce +))
