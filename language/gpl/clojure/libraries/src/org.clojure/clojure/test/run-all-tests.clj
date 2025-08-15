(require '[clojure.test :as test])

(test/deftest foo-test
  (test/testing "a"
    (test/is (= 1 1))))

; runs all tests in all namespaces
; optionally receives a regex to filter the desired namespaces
(clojure.test/run-all-tests)
