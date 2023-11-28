; get element from a collection (clojure.lang.IPersistentCollection)
; get-in does NOT work for sequences

;; map
(get-in
 {:a 1 :b {:b1 8 :b2 9} :c 2}
 [:b :b1])

;; vector
(get-in
 [0 1 [2 3]]
 [2 0]) ; out of bound returns nil

(get-in
 [[:a :b] [:c :d]]
 [0 1])
