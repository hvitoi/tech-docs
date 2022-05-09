(require '[clojure.test.check.generators :as gen])

;; vectors of dynamic size (increases that the number of vectors increase)
(def my-gen (gen/vector gen/small-integer))
(def my-gen (gen/vector gen/small-integer 5)) ; size 5
(def my-gen (gen/vector gen/small-integer 2 5)) ; size 2 to 5

(gen/sample my-gen)
