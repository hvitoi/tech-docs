(ns main
  (:require [clojure.test :as test]
            [clojure.string :as str]
            [clojure.math :as math]))

(defn reverse-integer
  [num]
  (->> num
       str
       str/reverse
       (map str)
       (map parse-long)
       (remove nil?)
       str/join
       parse-long
       (* (math/signum num))
       int))

(test/deftest reverse-integer-test
  (test/testing "reversing a integer"
    (test/is (= 0 (reverse-integer 0)))
    (test/is (= 5 (reverse-integer 5)))
    (test/is (= 51 (reverse-integer 15)))
    (test/is (= 9 (reverse-integer 90)))
    (test/is (= 9532 (reverse-integer 2359)))

    (test/is (= -5 (reverse-integer -5)))
    (test/is (= -51 (reverse-integer -15)))
    (test/is (= -9 (reverse-integer -90)))
    (test/is (= -9532 (reverse-integer -2359)))))

(test/run-test reverse-integer-test)
