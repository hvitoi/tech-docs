(require '[clojure.test.check.generators :as gen])

; return a constant
(def my-gen (gen/return :alpha))

(gen/sample my-gen)
