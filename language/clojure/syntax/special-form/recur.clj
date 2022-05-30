; create a recursion (call itself)
; avoid problems with stack overflow (tail recursion)
; can only recur from tail position!
; transforms a recursion into a loop!

(defn my-fn
  [function collection]
  (when (not (nil? (first collection)))
    (function first collection)
    (recur function (rest collection))))

(my-fn println (range 1000))

;; my own reduce (recursive)
(defn my-reduce
  ([elements]
   (my-reduce 0 elements))
  ([total elements]
   (if (seq elements)
     (recur (inc total) (next elements))
     total)))
