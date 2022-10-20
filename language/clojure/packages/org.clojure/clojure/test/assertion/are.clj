(require '[clojure.test :refer :all])

(deftest foo-test
  (testing "a"
    (are [x y] (= x y)
      2 (reduce + [1 1])
      3 (reduce + [1 1 1])
      4 (reduce + [1 1 1 1]))))
