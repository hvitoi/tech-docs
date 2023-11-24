; Peek (look) the next element to be removed (by an eventual pop)
; O(1)

; when using a peek with an atom, the whole function will be rerun case the atom changes in the middle

;; vector (ending)
(peek [0 1 2])

;; linked list (beginning)
(peek '(1 2 3))
