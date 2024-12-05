;; add/modify elements (with a value)

;; vec
(assoc ["a" "b" "c"] 3 "d") ; add new element (only to the last position + 1)
(assoc ["a" "b" "c"] 3 "d" 4 "e") ; add multiple elements
(assoc ["a" "b" "c"] 0 "z") ; modify existing element (index 0)

;; map
(assoc {:a "a", :b "b"} :c "c") ; add new element
(assoc {:a "a", :b "b"} :c "c" :d "d") ; add multiple elements
(assoc {:a "a", :b "b"} :a "z") ; modify existing element

(assoc nil :foo "baz")
