(require '[clojure.test :as test])

(defn fibonacci-recursive
  [n]
  (case n
    0 0
    1 1
    (+ (fibonacci-recursive (- n 1))
       (fibonacci-recursive (- n 2)))))

(defn fibonacci-reduce
  [n]
  (case n
    0 0
    1 1
    (loop [fibo [0 1]]
      (if (< n (count fibo))
        (last fibo)
        (recur
         (conj fibo
               (apply +
                      (take-last 2 fibo))))))))

(test/deftest foo-test
  (test/testing ""
    (test/is (= 0 (fibonacci-recursive 0)))
    (test/is (= 1 (fibonacci-recursive 1)))
    (test/is (= 610 (fibonacci-recursive 15)))

    (test/is (= 0 (fibonacci-reduce 0)))
    (test/is (= 1 (fibonacci-reduce 1)))
    (test/is (= 610 (fibonacci-reduce 15)))))

(test/run-test foo-test)
