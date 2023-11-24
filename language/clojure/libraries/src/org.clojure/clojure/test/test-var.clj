(require '[clojure.test :refer :all])


(defn fizz-buzz
  "That limited fizz-buzz function again"
  {:doc "Docs can be added like this too"
   :foo "Any attributes you fancy"
   :test (fn [] ; test runners will pick this
           (is (= "fizz-buzz" (fizz-buzz 15)))
           (is (= 3 (fizz-buzz 3))))}
  [n]
  (if (pos? (rem 15 n))
    "fizz-buzz"
    n))

(doc fizz-buzz)
(meta #'fizz-buzz)

; test-var
(test-var #'fizz-buzz)