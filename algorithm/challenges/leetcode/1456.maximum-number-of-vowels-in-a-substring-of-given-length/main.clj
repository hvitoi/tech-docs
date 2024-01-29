(require '[clojure.test :as test]
         '[clojure.string :as string])

(defn max-vowels
  [s k]
  (->> (inc (- (count s) k))
       range
       (map #(subs s % (+ % k)))
       (map #(re-seq #"[Aa|Ee|Ii|Oo|Uu]" %))
       (map count)
       sort
       last))

(test/deftest max-vowels-test
  (test/testing ""
    (test/is (= 3
                (max-vowels "abciiidef" 3)))
    (test/is (= 2
                (max-vowels "aeiou" 2)))
    (test/is (= 2
                (max-vowels "leetcode" 3)))))

(test/run-test max-vowels-test)
