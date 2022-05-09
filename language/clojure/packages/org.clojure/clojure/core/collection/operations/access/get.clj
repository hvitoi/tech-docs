; get element from a collection (clojure.lang.IPersistentCollection)

;; map
(def my-map {:key0 0 :key1 1 :key2 2})
(get my-map :key0)

;; vector
(def my-vector [0 1 2])
(get my-vector 0) ; out of bound returns nil
(get my-vector 99 -1) ; out of bound returns -1
