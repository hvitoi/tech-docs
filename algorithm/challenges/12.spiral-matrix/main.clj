(ns main
  (:require [clojure.test :as test]))

(defn spiral-matrix
  [n]
  (loop [num 1
         matrix (map (fn [_] (repeat n nil))
                     (range n))
         current-position [0 0]

         direction :right]
    (if (> num (n * n))
      matrix
      (recur
       (inc num)
       (assoc-in matrix current-position num)
       ()
       ()
       ;
       ))))

(test/deftest spiral-matrix-test
  (test/testing "Return a spiral matrix"
    (test/is (= [[1   2  3  4]
                 [12 13 14  5]
                 [11 16 15  6]
                 [10  9  8  7]]
                (spiral-matrix 4)))))

(test/run-test spiral-matrix-test)
