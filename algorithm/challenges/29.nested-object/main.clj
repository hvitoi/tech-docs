(ns main
  (:require [clojure.test :as test]))

(defn fibonacci
  [])

(test/deftest foo-test
  (test/testing ""
    (test/is (= nil
                (fibonacci)))))

(test/run-test foo-test)
