;; similar to atoms, but change the data asynchronously

(def a (agent 100))
(println @a)

