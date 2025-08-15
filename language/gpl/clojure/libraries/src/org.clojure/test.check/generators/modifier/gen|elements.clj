(require '[clojure.test.check.generators :as gen])

(gen/sample (gen/elements [:alpha :beta :gamma])); pick one of these elements