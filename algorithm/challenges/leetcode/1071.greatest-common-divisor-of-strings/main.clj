(require '[clojure.test :as test]
         '[clojure.string :as str])

(defn greatest-common-dividor
  [s1 s2]
  (loop [s s2
         size (count s2)]
    (if (str/includes? s1 s)
      s
      (recur))))

(test/deftest greatest-common-dividor-test
  (test/testing ""
    (test/is (= "ABC"
                (greatest-common-dividor "ABCABC" "ABC")))))

(test/run-test greatest-common-dividor-test)
