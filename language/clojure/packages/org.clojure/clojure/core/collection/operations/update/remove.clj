;; remove set of items from a collection
(remove #{"a" "b"} ["a" "b" "c" "d"])

;; remove with a function
(remove odd? [0 1 2 3 4 5])