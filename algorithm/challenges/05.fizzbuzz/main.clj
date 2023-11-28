(ns main
  (:require [clojure.test :as test]))

(defn fizzbuzz
  [n]
  (->> (range 1 (inc n))
       (map #(cond
               (and (zero? (mod % 3)) (zero? (mod % 5)))
               "fizzbuzz"
               (zero? (mod % 3))
               "fizz"
               (zero? (mod % 5))
               "buzz"
               :else %))))

(test/deftest fizzbuzz-test
  (test/testing "fizzbuzz for 15"
    (test/is (= [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]
                (fizzbuzz 15))))
  (test/testing "fizzbuzz for 0"
    (test/is (= []
                (fizzbuzz 0))))
  (test/testing "fizzbuzz for 1"
    (test/is (= [1]
                (fizzbuzz 1)))))

(test/run-test fizzbuzz-test)
