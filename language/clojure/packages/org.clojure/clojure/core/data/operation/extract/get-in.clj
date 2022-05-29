; get element from a collection (clojure.lang.IPersistentCollection)

;; map
(def my-map {:a 1 :b {:b1 8 :b2 9} :c 2})
(get-in my-map [:b :b1])

;; vector
(def my-vector [0 1 [2 3]])
(get-in my-vector [2 0]) ; out of bound returns nil
