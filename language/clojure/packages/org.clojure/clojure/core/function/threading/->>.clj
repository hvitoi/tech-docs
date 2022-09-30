;; THREAD LAST
;; threads to the last argument of the next function
(def my-map {:k1 1
             :k2 2})


(->> my-map
     vals ; (1 2)
     (map inc) ; (2 3)
     (reduce +)) ; 5

;; -> is usually used for collections
;; ->> is usually used fpr sequences
