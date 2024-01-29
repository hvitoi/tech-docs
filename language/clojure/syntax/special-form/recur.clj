; create a recursion (call itself)
; avoid problems with stack overflow (tail recursion)
; can only recur from tail position!
; transforms a recursion into a loop!

(defn first-even
  [coll]
  (if (even? (first coll))
    (first coll)
    (recur (next coll))))

(first-even [1 3 9 2 6 7]) ; => 2

;; my own reduce (recursive)
(defn my-reduce-sum
  ([elements] (my-reduce-sum 0 elements))
  ([sum elements]
   (if (seq elements)
     (recur (+ sum (first elements)) (next elements))
     sum)))

(my-reduce-sum [1 2 3 4])

;; ---

(def factorial
  (fn [n]
    (loop [cnt n
           acc 1]
      (if (zero? cnt)
        acc
        (recur (dec cnt) (* acc cnt))))))

(factorial 5)
