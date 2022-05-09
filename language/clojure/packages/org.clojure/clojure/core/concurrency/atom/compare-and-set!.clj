(def my-atom (atom 0))

; update conditionally
(compare-and-set! my-atom 110 120) ; if it's 110, then put 120