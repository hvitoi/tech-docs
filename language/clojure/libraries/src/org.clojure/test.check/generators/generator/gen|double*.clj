(require '[clojure.test.check.generators :as gen])

;; gen/double with additional info
(gen/sample (gen/double* {:infinite? false :NaN? false}))
