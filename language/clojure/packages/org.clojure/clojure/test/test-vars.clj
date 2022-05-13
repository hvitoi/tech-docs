(require '[clojure.test :refer :all])

; run a single test
(clojure.test/test-vars [#'namespace/function-test])
