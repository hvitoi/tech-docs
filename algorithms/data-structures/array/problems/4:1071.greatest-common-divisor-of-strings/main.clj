(require '[clojure.test :as test]
         '[clojure.string :as str])

(defn greatest-common-dividor
  [s1 s2]
  (let [s (str s1 s2)]
    (->> (range 1 (count s))
         (map #(partition-all % s))
         (reduce (fn [_ split]
                   (if (apply = split)
                     (reduced (str/join (first split)))
                     ""))))))

(test/deftest greatest-common-dividor-test
  (test/testing ""
    (test/is (= "ABC"
                (greatest-common-dividor "ABCABC" "ABC")))
    (test/is (= "AB"
                (greatest-common-dividor "ABABAB" "ABAB")))
    (test/is (= ""
                (greatest-common-dividor "LEET" "CODE")))))

(test/run-test greatest-common-dividor-test)
