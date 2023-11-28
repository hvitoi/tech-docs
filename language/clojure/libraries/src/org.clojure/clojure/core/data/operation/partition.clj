; partition the vector in chunks of n elements
;; items that do not make a complete partition and are dropped.
(partition 2 (range 19)) ; 18 is dropped

; set a "step" (each new partition starts with a multiple of the step)
(partition 3 5 (range 20))

; when step is lower than the partition size, elements are repeated
(partition 3 2 (range 20))

; set a pad to fill out the remaining spaces of the last partition (and do no drop any)
(partition 3 3 [:a :b :c] (range 20))
