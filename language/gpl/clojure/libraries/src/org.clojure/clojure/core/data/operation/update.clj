;; add/modify elements (with a function)

;; map
(update {:a 1, :b 2, :c 3} :a inc) ; modify
(update {:a 1, :b 2, :c 3} :d str) ; add (receives a nil and the current value does't exist)
(update {:a 1, :b 2, :c 3} :c str " is now a string") ; function with args (thread first)
(update {:a 1, :b 2, :c 3} :d merge {"a" "a"})

;; vector
(update [0 1 2] 0 inc) ; increment the position 0 by 1
(update [0 1 2] 2 concat [3 4]) ; concat to the last position 
