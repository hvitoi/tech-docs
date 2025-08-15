(require '[clojure.test :as test])

(test/deftest foo-test
  (test/testing "a"
    (test/is (= 1 1))))

; run a test by its symbol
; returns a map with the summary
(test/run-test foo-test)
