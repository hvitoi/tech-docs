(ns main
  (:require [clojure.test :as test]))

(defn famous-char
  [string]
  (as-> string $
    (group-by identity $)
    (update-vals $ count)
    (reduce-kv (fn [m k v]
                 (if (> v (:occurences m))
                   {:char k :occurences v}
                   m))
               {:char nil :occurences 0} $)
    (:char $)))

(defn famous-char-with-frequency
  [string]
  (->> (frequencies string)
       (reduce-kv (fn [m k v]
                    (if (> v (get m 1)) [k v] m))
                  [nil 0])
       first))

(defn famous-char-with-frequency-and-sort-by
  [string]
  (->> (frequencies string)
       (sort-by second)
       last
       first))

(test/deftest famous-char-test
  (test/testing "return the most famous char in a string"
    (test/is (= \a (famous-char "abca")))
    (test/is (= \a (famous-char-with-frequency "abca")))
    (test/is (= \b (famous-char-with-frequency-and-sort-by "abbbca")))))

(test/run-test (famous-char-test))
