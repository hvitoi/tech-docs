; get element from a collection (clojure.lang.IPersistentCollection)

;; map
(def data {:key0 0 :key1 1 :key2 2})
(get data :key0)

;; vector
(def data2 [0 1 2])
(get data2 0) ; out of bound returns nil
(get data2 99 -1) ; out of bound returns -1
