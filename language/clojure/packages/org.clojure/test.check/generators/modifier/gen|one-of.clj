(require '[clojure.test.check.generators :as gen])

; one or other
(def my-gen (gen/one-of [gen/small-integer gen/Keyword]))

(gen/sample my-gen)
