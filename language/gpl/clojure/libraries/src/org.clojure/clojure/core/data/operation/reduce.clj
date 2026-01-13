
(reduce + [1 2 3]) ; sum up all elements (starts with 0)
(reduce + 10 [1 2 3]) ; sum up all elements (starts with 10)
(reduce + 10 nil)
(reduce + 10 [])
(reduce (fn [acc el] (concat acc [el])) [] [1 2])

; custom aggregation function
(reduce (fn [acc n]
          (str acc ":" n))
        [1 1 2 3 5 8 13 21])

;; my own reduce (recursive)
(defn my-reduce
  ([elements]
   (my-reduce 0 elements))
  ([total elements]
   (if (seq elements)
     (recur (inc total) (next elements))
     total)))

;; break out of reduce (stop the process before the input sequence is exhausted)
(reduce (fn [acc n]
          (if (nil? n)
            (reduced acc) ; "reduced" stops with a nil
            (str acc ":" n)))
        [1 1 2 3 5 8 nil 13 21])

;; if no start value for reduce is used, the first value of the array is used and the reduce starts from the second element

; exponential
(reduce * (repeat n x))

(reduce
 (fn [m [k v]]
   (println m k v))
 {}
 {:a "a" :b "b"}) ; same as reduce-kv
