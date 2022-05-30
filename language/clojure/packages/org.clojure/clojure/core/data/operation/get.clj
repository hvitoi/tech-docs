; get element from a collection (clojure.lang.IPersistentCollection)

;; map
(get {:a "alpha" :b "beta"} :a)

;; vector
(get ["a" "b" "c"] 0) ; "a"
(get ["a" "b" "c"] 99) ; out of bound returns -1
(get ["a" "b" "c"] 'x) ; invalid returns nil
