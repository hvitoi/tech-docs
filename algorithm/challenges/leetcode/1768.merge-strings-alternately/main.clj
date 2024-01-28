(require '[clojure.test :as test])

(defn merge-strings
  [word1 word2]
  (loop [w1 (seq word1)
         w2 (seq word2)
         merged ""]
    (if (or w1 w2)
      (recur w2
             (next w1)
             (str merged (first w1)))
      merged)))

(test/deftest merge-strings-test
  (test/testing "Merge two strings with same size"
    (test/is (= "apbqcr"
                (merge-strings "abc" "pqr"))))
  (test/testing "Merge two strings with different sizes"
    (test/is (= "apbqrs"
                (merge-strings "ab" "pqrs")))))

(test/run-test merge-strings-test)
