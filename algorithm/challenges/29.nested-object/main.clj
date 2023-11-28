(ns main
  (:require [clojure.test :as test]))

(defn foo
  [])

(test/deftest foo-test
  (test/testing ""
    (test/is (= nil
                (foo)))))

(test/run-test foo-test)
