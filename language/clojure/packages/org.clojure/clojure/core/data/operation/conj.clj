;; conj(oin): add a new element
;; The new element is added to the easier place for the given data structure
;; Behaves differently for each implementation of a collection
;; O(1)

;; vec (ending)
(conj [1 2 3] 4)
(conj [1 2 3] 4 5 6) ; multiple elements

;; seq (beginning)
(conj (seq [1 2 3]) 4)

;; list (beginning)
(conj '(1 2 3) 4)

;; set (no order)
(conj #{1 2 3} 4)

;; map (no order)
(conj {:a 1 :b 2 :c 3} {:d 4})
(conj {:a 1 :b 2 :c 3} {:c 4}) ; replace
