(require '[clojure.test.check.generators :as gen])

;; 10 samples by default
(gen/sample gen/boolean)

;; 3 samples
(gen/sample gen/boolean 3)

