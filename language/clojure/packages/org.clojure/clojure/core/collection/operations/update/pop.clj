; Remove element from the end and return the rest
; Behaves differently for each implementation of a collection
; O(1)

;; vector (ending)
(pop [0 1 2])

;; linked list (beginning)
(pop '(1 2 3))

