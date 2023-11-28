(require '[clojure.test :as test])

(defn fizz-buzz
  "That limited fizz-buzz function again"
  {:doc "Docs can be added like this too"
   :foo "Any attributes you fancy"
   :test (fn [] ; test runners will pick this
           (test/is (= "fizz-buzz" (fizz-buzz 15)))
           (test/is (= 3 (fizz-buzz 3))))}
  [n]
  (if (pos? (rem 15 n))
    "fizz-buzz"
    n))

(doc fizz-buzz)
(meta #'fizz-buzz)

; Run a test defined in a `:test` metadata
(test/test-var #'fizz-buzz)
