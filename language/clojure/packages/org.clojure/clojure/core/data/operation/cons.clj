; returns a sequence
; append the new element in the beginning of the list
(cons 3 (seq [4 5 6])) ; seq -> seq
(cons 3 [4 5 6]) ; vector -> seq
(cons 3 #{3 5 6}) ; set -> seq
