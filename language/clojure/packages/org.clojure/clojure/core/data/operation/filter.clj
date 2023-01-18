; Filter elements in which the predicate returns true

;; vector
(filter even? [0 1 2])

;; map
(defn even??
  [[k v]]
  (= 0 (rem v 2)))

(filter even? {:a 1, :b 2, :c 3})
