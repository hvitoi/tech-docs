(require '[clojure.test :as test])

(test/deftest foo-test
  (test/testing "a"
    (test/is (= 1 1))))

; runs all tests in a namespace (defaults to the current namespace)
; returns a map with the summary
(test/run-tests)
(test/run-tests 'user)
