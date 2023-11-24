(require '[clojure.test :refer :all])

;; define a testing element
(deftest foo-test
  (testing "that one equals to one"
    (is (= 1 1)))
  (testing "that zero equals to zero"
    (is (= 0 0))))
