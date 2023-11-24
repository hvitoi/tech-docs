(defn positive-numbers
  ([] (positive-numbers 1))
  ([n] (lazy-seq (cons n (positive-numbers (inc n))))))
