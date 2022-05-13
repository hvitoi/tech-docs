(def map1 {:k1 "v1" :k2 "v2"}) ; commas are optional
(def map2 {1 42, 2 1.5, "pet" 'cat})

;; nested maps
(def map3 {:k1 {:a "a" :b "b"}
           :k2 {:c "c" :d "d"}})

;; Map as a fuction
(map1 :k1)

;; Keyword as a function 
(:k1 map1) ; better! returns nil if not found
(:k1 map1 "nothing") ; with default value
(:a (:k1 map3)) ; nested value
