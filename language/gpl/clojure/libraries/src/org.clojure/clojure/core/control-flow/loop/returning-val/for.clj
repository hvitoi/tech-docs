;; x is the outer loop (i)
;; y is the inner loop (j)
(for [x [:a :b :c]
      y [1 2 3 4]]
  [x y])

;; prepare a seq of the even values
;; from the first six multiples of three
(for [x [0 1 2 3 4 5]
      :let [y (* x 3)
            d' (- x y) ; d' is a symbol like any other
            d (Math/abs d')]
      :when (even? y)]
  y)

(for [x "abc"] x)
