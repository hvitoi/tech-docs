;; break out of reduce (stop the process before the input sequence is exhausted)
(reduce (fn [acc n]
          (if (nil? n)
            (reduced acc) ; "reduced" stops with a nil
            (str acc ":" n)))
        [1 1 2 3 5 8 nil 13 21])
