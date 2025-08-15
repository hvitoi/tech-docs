(sort [3 2 1])
(sort ["c" "b" "a"])

; reverse
(sort ["c" "b" "a"])
(sort #(compare %2 %1) ["a" "c" "b"]) ; inverted compare

(sort > [1 2 3])
(sort > ["c" "a" "b"])

(sort #(compare (get %2 1)
                (get %1 1))
      {:a 2 :b 1 :c 3})
