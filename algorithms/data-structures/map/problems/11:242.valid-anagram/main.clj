(require '[clojure.test :as test]
         '[clojure.string :as str])

(defn anagram?
  [s1 s2]
  (let [char-map (fn [s]
                   (->> s
                        str/lower-case
                        (re-seq #"[A-z]")
                        frequencies))]
    (= (char-map s1)
       (char-map s2))))

(test/deftest anagram?-test
  (test/testing "Check if the strings are anagrams"
    (test/is (true? (anagram? "hello" "llohe")))
    (test/is (true? (anagram? "Whoa!    Hi!!!!" "Hi! Whoa!")))))

(test/run-test anagram?-test)
