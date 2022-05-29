; update a collection with a function

;; map
(def data {:k1 1, :k2 2, :k3 []})
(update data :k1 inc) ; increment value from key :k1 by 1
(update data :k3 conj "newitem") ; args are passed after the function

;; vector
(def data2 [1 2])
(update data2 0 inc) ; increment the position 0 by 1
(update data2 2 concat [3 4]) ; concat to the last position 
