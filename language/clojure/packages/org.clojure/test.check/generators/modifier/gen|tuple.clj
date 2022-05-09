(require '[clojure.test.check.generators :as gen])

(def my-gen ((gen/tuple [gen/Keyword gen/boolean])))
(def my-gen ((gen/tuple [gen/Keyword (gen/return :alpha) gen/boolean]))) ; tuple with a fixed value 

(gen/sample my-gen)
