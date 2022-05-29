
;; vector
(def data ["a" "b" "c"])

; verify if an index exists
(contains? data 2) ; true
(contains? data 3) ; false

;; map
(def data2 {:a "a", :b "b"})

; verify if a keyword exists
(contains? data2 :a) ; true
(contains? data2 :z) ; false
