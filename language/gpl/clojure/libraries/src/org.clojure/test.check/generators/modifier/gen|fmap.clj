(require '[clojure.test.check.generators :as gen]
         '[clojure.string :as str])

; apply a function to a generator and return a generator
(def my-gen
  (gen/fmap str/join (gen/vector gen/char-alphanumeric 5 10)))

(gen/sample my-gen)
