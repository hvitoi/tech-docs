(require '[clojure.test :refer :all])

(defn my-fn []
  (throw (ex-info "some error message" {})))


(deftest my-fn-test
  ; verify if a specific exception type is thrown
  (testing "a"
    (is (thrown? clojure.lang.ExceptionInfo (my-fn)))))
