; return a random elements from a collection
(rand-nth [1 2 3 4 5])
(rand-nth [true false])

(apply str (repeatedly 5 #(rand-nth "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")))
