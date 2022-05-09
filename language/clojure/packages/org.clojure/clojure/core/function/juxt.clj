(def my-vector [0 1 2])

; execute two functions at the same time (not after each other)
; the evaluation is returned as a vector
(def run-together (juxt peek pop))
(run-together my-vector); [2 [0 1]]

(let [[res1 res2] (run-together my-vector)]
  (println res1 res2))
