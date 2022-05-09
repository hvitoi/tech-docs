(require '[clojure.test :refer :all])

; define a test block
(deftest foo-test
  (testing "a"
    (is (= 1 1))))