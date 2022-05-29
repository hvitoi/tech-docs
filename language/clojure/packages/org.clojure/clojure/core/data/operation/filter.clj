; Filter elements in which the predicate returns true

;; vector
(filter even? [0 1 2])

;; map
(defn even??
  [[k v]]
  (= 0 (rem v 2)))

(filter even?? {:k0 0, :k1 1, :k2 2})
