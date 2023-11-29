(require '[clojure.test :as test])

(defn number-of-vowels
  [string]
  (->> string
       (re-seq #"[aeiou]")
       count))

(test/deftest number-of-vowels-test
  (test/testing "Check the number of vowels in a string"
    (test/is (= 5 (number-of-vowels "abcdefghijklmnopqrstuvwxyz")))
    (test/is (= 0 (number-of-vowels "bcdfghjkl")))))

(test/run-test number-of-vowels-test)
