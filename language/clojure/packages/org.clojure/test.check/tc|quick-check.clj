(require '[clojure.test.check :as tc]
         '[clojure.test.check.generators :as gen]
         '[clojure.test.check.properties :as prop #?@(:cljs [:include-macros true])])

(def property
  (prop/for-all [my-vector (gen/vector gen/string-alphanumeric 3)]
                (println my-vector)
                (= 3 (count my-vector))))

;; test a property n times
(tc/quick-check 10 property)

;; {:num-tests 10,
;;  :pass? true,
;;  :result true,
;;  :seed 1648235740275,
;;  :time-elapsed-ms 2}
