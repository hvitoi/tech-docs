(ns main
  (:require [clojure.test :as test]))

(defn spiral-matrix
  [n])

(test/deftest spiral-matrix-test
  (test/testing "Return a spiral matrix"
    (test/is (= [[1   2  3  4]
                 [12 13 14  5]
                 [11 16 15  6]
                 [10  9  8  7]]
                (spiral-matrix 4)))))

(test/run-test spiral-matrix-test)
