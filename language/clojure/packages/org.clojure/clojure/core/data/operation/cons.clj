;; cons: add new list (to the beginning always)
;; Always return a sequence

(cons 0 (seq [1 2 3])) ; seq -> seq
(cons 0 [1 2 3]) ; vector -> seq
(cons 0 #{1 2 3}) ; set -> seq
(cons 0 '(1 2 3)) ; list -> seq
