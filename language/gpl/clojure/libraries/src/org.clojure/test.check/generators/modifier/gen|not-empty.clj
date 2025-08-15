(require '[clojure.test.check.generators :as gen])

(def my-gen (gen/not-empty (gen/vector gen/boolean)))

(gen/sample my-gen)