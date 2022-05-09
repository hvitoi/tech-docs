; create a recursion (call itself)
; avoid problems with stack overflow (tail recursion)
; can only recur from tail position!
; transforms a recursion into a loop!

(defn my-fn
  [function collection]
  (if (not (nil? (first collection)))
    (do (function first collection)
        (recur function (rest collection)))))

(my-fn println (range 1000))