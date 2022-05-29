; update a collection with a function

;; map
(def my-map {:k1 1, :k2 2, :k3 []})
(update my-map :k1 inc) ; increment value from key :k1 by 1
(update my-map :k3 conj "newitem") ; args are passed after the function

;; vector
(def my-vector [1 2])
(update my-vector 0 inc) ; increment the position 0 by 1
(update my-vector 2 concat [3 4]) ; concat to the last position 
