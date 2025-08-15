
;; vector (verify if an index exists)
(def data ["a" "b" "c"])
(contains? data 2) ; true
(contains? data 3) ; false

;; map (verify if a keyword exists)
(def data2 {:a "a", :b "b"})
(contains? data2 :a) ; true
(contains? data2 :z) ; false

;; set
(contains? #{:a :b} :c)
