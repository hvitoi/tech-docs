(ns main
  (:require [clojure.test :as test]))

(defn fibonacci
  [n]
  (case n
    1 0
    2 1
    (+ (fibonacci (- n 1)) (fibonacci (- n 2)))))

(test/deftest foo-test
  (test/testing ""
    (test/is (= 377
                (fibonacci 15)))))

(test/run-test foo-test)
