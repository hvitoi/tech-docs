(require
 '[clojure.test.check.generators :as gen]
 '[clojure.test.check.properties :as prop #?@(:cljs [:include-macros true])])

;; create a property
;; a property is the combination of "generators" and "assertions"
(def property
  (prop/for-all [my-vector (gen/vector gen/string-alphanumeric 3)] ;; variables with generators
                (println my-vector)
                (= 3 (count my-vector)))) ;; assertion

;; property with multiple variables
(def property
  (prop/for-all [my-vector (gen/vector gen/string-alphanumeric 3)
                 my-number  gen/small-integer]
                (println my-vector my-number)
                (= 4 (count (conj my-vector my-number)))))
