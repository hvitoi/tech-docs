(require '[clojure.test :as test])

; define a test block
(test/deftest foo-test
  (test/testing "a"
    (test/is (= 1 1))))
