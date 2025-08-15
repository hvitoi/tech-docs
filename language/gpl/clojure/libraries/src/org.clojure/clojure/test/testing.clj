(require '[clojure.test :as test])

(test/deftest foo-test
  (test/testing "a"
    (test/is (= 1 1))))
