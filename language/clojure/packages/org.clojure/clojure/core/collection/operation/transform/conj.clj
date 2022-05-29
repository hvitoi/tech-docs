;; Add a new element
;; The new element is added to the easier place for the given data structure
;; Behaves differently for each implementation of a collection
; O(1)

;; vector (ending)
(conj [1 2 3] 4)
(conj [1 2 3] 4 5 6) ; add multiple elements


;; sequence (beginning)
(conj (seq [1 2 3]) 4)


;; linked list (beginning)
(conj '(1 2 3) 4)

;; set (ending)
(conj #{1 2 3} 4)