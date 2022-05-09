;; produce a seq of all pairs drawn from two vectors
(for [x ['a 'b 'c]
      y [1 2 3]]
  [x y])
;;=> ([a 1] [a 2] [a 3] [b 1] [b 2] [b 3] [c 1] [c 2] [c 3])


;; prepare a seq of the even values 
;; from the first six multiples of three
(for [x [0 1 2 3 4 5]
      :let [y (* x 3)
            d' (- x y) ; d' is a symbol like any other
            d (Math/abs d')]
      :when (even? y)]
  y)
;;=> (0 6 12)

