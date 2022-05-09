; partition the vector in chunks of n elements

(->> [1 1 2 3 5 8 13 21]
     (partition 2))