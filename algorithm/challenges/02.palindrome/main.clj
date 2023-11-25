(ns main
  (:require [clojure.test :as test]
            [clojure.string :as str]))

(defn palindrome?-with-reverse
  [word]
  (= (str/reverse word) word))

(defn palindrome?-with-map
  [word]
  (->> (map-indexed
        (fn [i char]
          (let [associated-char (get word (- (count word) i 1))]
            (= char associated-char))) ; not optimal because it could go until the middle of the vector only
        word)
       (every? true?)))

(test/deftest palindrome?-test
  (test/testing "a valid palindrome"
    (test/is (true? (palindrome?-with-reverse "abIba")))
    (test/is (true? (palindrome?-with-map "abIba"))))
  (test/testing "an invalid palindrome"
    (test/is (false? (palindrome?-with-reverse " abba")))
    (test/is (false? (palindrome?-with-map " abba")))))

(palindrome?-test)
