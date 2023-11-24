(require '[clojure.test :refer :all])

;; "is" evaluates a truthy input as success
(deftest foo-test

  ; simple evaluation
  (testing "a"
    (is (= 1 1)))

  ; deep equality
  (testing "b"
    (is (= {:a "a", :b [1 2 3]} {:a "a", :b [1 2 3]})))

  ; evaluate to success if the expcetion is ClassCastException and the message is something specified
  (testing "d"
    (is (try
          (inc 1)
          (catch ClassCastException e
            (= {:something "anything"} (ex-data e)))))))
