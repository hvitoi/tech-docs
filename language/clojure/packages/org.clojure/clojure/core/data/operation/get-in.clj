; get element from a collection (clojure.lang.IPersistentCollection)

;; map
(def data {:a 1 :b {:b1 8 :b2 9} :c 2})
(get-in data [:b :b1])

;; vector
(def data2 [0 1 [2 3]])
(get-in data2 [2 0]) ; out of bound returns nil
