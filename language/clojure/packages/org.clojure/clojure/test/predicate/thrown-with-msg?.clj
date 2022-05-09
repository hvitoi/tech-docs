(require '[clojure.test :refer :all])

(defn my-fn []
  (throw (ex-info "some error message" {})))

(deftest my-fn-test
  ; verify if a specific exception type and message is thrown
  (testing "a"
    (is (thrown-with-msg? clojure.lang.ExceptionInfo "this must be the exeption message" (my-fn)))))
