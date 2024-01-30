; Same as "map" but nil values are removed

;; vector
(keep identity [9 "a" true false nil])
(map identity [9 "a" true false nil])
