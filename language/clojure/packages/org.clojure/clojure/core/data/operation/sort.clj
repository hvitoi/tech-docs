(sort [3 2 1])
(sort ["c" "b" "a"])

; reverse
(sort ["c" "b" "a"])
(sort #(compare %2 %1) ["a" "c" "b"])

(sort > [1 2 3])
(sort > ["c" "a" "b"])
